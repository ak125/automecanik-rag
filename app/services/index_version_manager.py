"""Index Version Manager - @latest/@rollback support for RAG collections.

P3 FEATURE: Versioned indexes with rollback capability.

Usage:
    manager = IndexVersionManager()

    # Create new version
    version = manager.create_version("Prod_Chatbot")
    # Returns: "Prod_Chatbot_v20260102_120000"

    # Get current @latest
    latest = manager.get_latest("Prod_Chatbot")

    # Rollback to previous
    manager.rollback("Prod_Chatbot")

    # Cleanup old versions (keep last N)
    manager.cleanup("Prod_Chatbot", keep_last=3)
"""

import os
import json
import logging
from datetime import datetime
from typing import Optional
from pathlib import Path

logger = logging.getLogger(__name__)

MANIFEST_PATH = os.getenv("INDEX_MANIFEST_PATH", "/opt/automecanik/rag/data/index_manifest.json")


class IndexVersion:
    """Represents a single index version."""

    def __init__(
        self,
        collection_name: str,
        version_id: str,
        created_at: str,
        document_count: int = 0,
        status: str = "active",
        metadata: Optional[dict] = None,
    ):
        self.collection_name = collection_name
        self.version_id = version_id
        self.created_at = created_at
        self.document_count = document_count
        self.status = status
        self.metadata = metadata or {}

    @property
    def full_name(self) -> str:
        return f"{self.collection_name}_{self.version_id}"

    def to_dict(self) -> dict:
        return {
            "collection_name": self.collection_name,
            "version_id": self.version_id,
            "full_name": self.full_name,
            "created_at": self.created_at,
            "document_count": self.document_count,
            "status": self.status,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "IndexVersion":
        return cls(
            collection_name=data["collection_name"],
            version_id=data["version_id"],
            created_at=data["created_at"],
            document_count=data.get("document_count", 0),
            status=data.get("status", "active"),
            metadata=data.get("metadata", {}),
        )


class IndexManifest:
    """Manages the manifest file tracking all index versions."""

    def __init__(self, path: str = MANIFEST_PATH):
        self.path = Path(path)
        self._data: dict = {"collections": {}, "aliases": {}}
        self._load()

    def _load(self):
        if self.path.exists():
            try:
                with open(self.path, "r") as f:
                    self._data = json.load(f)
            except Exception as e:
                logger.error(f"Failed to load manifest: {e}")
                self._data = {"collections": {}, "aliases": {}}
        else:
            self.path.parent.mkdir(parents=True, exist_ok=True)

    def _save(self):
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, "w") as f:
                json.dump(self._data, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save manifest: {e}")

    def add_version(self, version: IndexVersion):
        collection = version.collection_name
        if collection not in self._data["collections"]:
            self._data["collections"][collection] = []
        self._data["collections"][collection].append(version.to_dict())
        self._save()

    def get_versions(self, collection_name: str) -> list[IndexVersion]:
        versions = self._data["collections"].get(collection_name, [])
        result = [IndexVersion.from_dict(v) for v in versions]
        result.sort(key=lambda x: x.created_at, reverse=True)
        return result

    def set_alias(self, collection_name: str, alias: str, version_id: str):
        key = f"{collection_name}:{alias}"
        self._data["aliases"][key] = {
            "collection_name": collection_name,
            "alias": alias,
            "version_id": version_id,
            "updated_at": datetime.now().isoformat(),
        }
        self._save()

    def get_alias(self, collection_name: str, alias: str) -> Optional[str]:
        key = f"{collection_name}:{alias}"
        alias_data = self._data["aliases"].get(key)
        return alias_data["version_id"] if alias_data else None

    def remove_version(self, collection_name: str, version_id: str):
        versions = self._data["collections"].get(collection_name, [])
        self._data["collections"][collection_name] = [
            v for v in versions if v["version_id"] != version_id
        ]
        self._save()


class IndexVersionManager:
    """Manages versioned indexes with @latest/@rollback support."""

    def __init__(self, weaviate_url: str = None):
        self.weaviate_url = weaviate_url or os.getenv("WEAVIATE_URL", "http://localhost:8080")
        self.manifest = IndexManifest()

    def generate_version_id(self) -> str:
        now = datetime.now()
        return f"v{now.strftime('%Y%m%d')}_{now.strftime('%H%M%S')}"

    def create_version(
        self,
        base_collection: str,
        document_count: int = 0,
        metadata: Optional[dict] = None,
    ) -> IndexVersion:
        version_id = self.generate_version_id()
        version = IndexVersion(
            collection_name=base_collection,
            version_id=version_id,
            created_at=datetime.now().isoformat(),
            document_count=document_count,
            status="active",
            metadata=metadata or {},
        )
        self.manifest.add_version(version)
        logger.info(f"Created index version: {version.full_name}")
        return version

    def promote_to_latest(self, base_collection: str, version_id: str):
        current_latest = self.manifest.get_alias(base_collection, "@latest")
        if current_latest:
            self.manifest.set_alias(base_collection, "@previous", current_latest)
        self.manifest.set_alias(base_collection, "@latest", version_id)
        logger.info(f"Promoted {version_id} to @latest")

    def get_latest(self, base_collection: str) -> Optional[IndexVersion]:
        version_id = self.manifest.get_alias(base_collection, "@latest")
        if not version_id:
            versions = self.manifest.get_versions(base_collection)
            return versions[0] if versions else None
        for v in self.manifest.get_versions(base_collection):
            if v.version_id == version_id:
                return v
        return None

    def get_previous(self, base_collection: str) -> Optional[IndexVersion]:
        version_id = self.manifest.get_alias(base_collection, "@previous")
        if not version_id:
            return None
        for v in self.manifest.get_versions(base_collection):
            if v.version_id == version_id:
                return v
        return None

    def rollback(self, base_collection: str) -> bool:
        previous = self.get_previous(base_collection)
        if not previous:
            logger.error("No @previous version available for rollback")
            return False
        current = self.get_latest(base_collection)
        self.manifest.set_alias(base_collection, "@latest", previous.version_id)
        if current:
            self.manifest.set_alias(base_collection, "@previous", current.version_id)
        logger.info(f"Rolled back to {previous.version_id}")
        return True

    def list_versions(self, base_collection: str) -> list[dict]:
        versions = self.manifest.get_versions(base_collection)
        latest_id = self.manifest.get_alias(base_collection, "@latest")
        previous_id = self.manifest.get_alias(base_collection, "@previous")
        result = []
        for v in versions:
            info = v.to_dict()
            aliases = []
            if v.version_id == latest_id:
                aliases.append("@latest")
            if v.version_id == previous_id:
                aliases.append("@previous")
            info["aliases"] = aliases
            result.append(info)
        return result


_version_manager: Optional[IndexVersionManager] = None


def get_version_manager() -> IndexVersionManager:
    global _version_manager
    if _version_manager is None:
        _version_manager = IndexVersionManager()
    return _version_manager
