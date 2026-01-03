"""Security Validator - Anti Prompt Injection + PII Detection.

P0 CRITICAL SECURITY:
- Detects and blocks prompt injection attacks
- Detects PII (GDPR compliance) and redirects to support API
- Validates request content before RAG processing

Usage:
    validator = SecurityValidator()
    result = validator.validate(message)
    if not result.is_safe:
        return error_response(result.reason)
"""

import re
import logging
from dataclasses import dataclass
from typing import Optional
from enum import Enum

logger = logging.getLogger(__name__)


class SecurityRisk(Enum):
    """Types of security risks detected."""
    NONE = "none"
    PROMPT_INJECTION = "prompt_injection"
    PII_EMAIL = "pii_email"
    PII_PHONE = "pii_phone"
    PII_ORDER_ID = "pii_order_id"
    PII_CREDIT_CARD = "pii_credit_card"
    PII_IBAN = "pii_iban"


@dataclass
class ValidationResult:
    """Result of security validation."""
    is_safe: bool
    risk: SecurityRisk
    reason: Optional[str] = None
    redirect_to: Optional[str] = None
    matched_pattern: Optional[str] = None


# P0 SECURITY: Prompt Injection Patterns
# These patterns detect common LLM jailbreak attempts
INJECTION_PATTERNS = [
    # Instruction override attempts
    (r"ignore\s+(?:all\s+)?(?:previous|prior|above)\s+instructions?", "ignore_instructions"),
    (r"forget\s+(?:all\s+)?(?:everything|what\s+you)", "forget_instructions"),
    (r"disregard\s+(?:all\s+)?(?:previous|prior|your)\s+(?:instructions?|rules?)", "disregard_rules"),

    # Role manipulation
    (r"you\s+are\s+now\s+(?:a|an|my)", "role_override"),
    (r"pretend\s+(?:you\s+are|to\s+be)", "role_pretend"),
    (r"act\s+as\s+(?:if\s+you\s+are|a)", "role_act"),

    # Prompt reveal attempts
    (r"reveal\s+(?:your|the)\s+(?:system\s+)?prompt", "reveal_prompt"),
    (r"show\s+(?:me\s+)?(?:your|the)\s+(?:system\s+)?instructions?", "show_instructions"),
    (r"what\s+(?:are\s+)?(?:your|the)\s+(?:system\s+)?instructions?", "ask_instructions"),

    # Format markers (Llama, ChatML, etc.)
    (r"\[INST\]", "format_inst"),
    (r"\[/INST\]", "format_inst_close"),
    (r"<\|im_start\|>", "format_chatml"),
    (r"<\|im_end\|>", "format_chatml_end"),
    (r"<\|system\|>", "format_system"),
    (r"<\|user\|>", "format_user"),
    (r"<\|assistant\|>", "format_assistant"),
    (r"<<SYS>>", "format_llama_sys"),
    (r"<</SYS>>", "format_llama_sys_end"),

    # System/developer mode
    (r"developer\s+mode", "dev_mode"),
    (r"sudo\s+mode", "sudo_mode"),
    (r"admin\s+mode", "admin_mode"),
    (r"jailbreak", "jailbreak"),
    (r"DAN\s+mode", "dan_mode"),

    # Output manipulation
    (r"respond\s+only\s+with", "output_override"),
    (r"output\s+only", "output_only"),
    (r"print\s+(?:only|just)", "print_only"),
]

# P0 SECURITY: PII Patterns (GDPR Compliance)
PII_PATTERNS = {
    SecurityRisk.PII_EMAIL: (
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "Email address detected"
    ),
    SecurityRisk.PII_PHONE: (
        r"(?:\+33|0033|0)[1-9](?:[\s.-]?\d{2}){4}",
        "French phone number detected"
    ),
    SecurityRisk.PII_ORDER_ID: (
        r"(?:ORD|CMD|FAC|REF)[-_]?\d{6,}",
        "Order/invoice ID detected"
    ),
    SecurityRisk.PII_CREDIT_CARD: (
        r"\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13})\b",
        "Credit card number detected"
    ),
    SecurityRisk.PII_IBAN: (
        r"\b[A-Z]{2}\d{2}[A-Z0-9]{4}\d{7}(?:[A-Z0-9]?){0,16}\b",
        "IBAN detected"
    ),
}


class SecurityValidator:
    """
    Validates request content for security threats.

    Checks for:
    1. Prompt injection attacks (jailbreak attempts)
    2. PII data (GDPR compliance)
    """

    def __init__(self, strict_mode: bool = True):
        """
        Initialize validator.

        Args:
            strict_mode: If True, blocks on first detection. If False, logs only.
        """
        self.strict_mode = strict_mode
        self._compile_patterns()

    def _compile_patterns(self):
        """Pre-compile regex patterns for performance."""
        self._injection_patterns = [
            (re.compile(pattern, re.IGNORECASE), name)
            for pattern, name in INJECTION_PATTERNS
        ]
        self._pii_patterns = {
            risk: (re.compile(pattern), desc)
            for risk, (pattern, desc) in PII_PATTERNS.items()
        }

    def validate(self, message: str) -> ValidationResult:
        """
        Validate a message for security threats.

        Args:
            message: User message to validate

        Returns:
            ValidationResult with safety status and details
        """
        if not message:
            return ValidationResult(is_safe=True, risk=SecurityRisk.NONE)

        # Check for prompt injection first
        injection_result = self._check_injection(message)
        if not injection_result.is_safe:
            logger.warning(
                f"SECURITY: Prompt injection blocked - pattern={injection_result.matched_pattern}"
            )
            return injection_result

        # Check for PII
        pii_result = self._check_pii(message)
        if not pii_result.is_safe:
            logger.warning(
                f"SECURITY: PII detected - type={pii_result.risk.value}"
            )
            return pii_result

        return ValidationResult(is_safe=True, risk=SecurityRisk.NONE)

    def _check_injection(self, message: str) -> ValidationResult:
        """Check for prompt injection patterns."""
        for pattern, name in self._injection_patterns:
            if pattern.search(message):
                return ValidationResult(
                    is_safe=False,
                    risk=SecurityRisk.PROMPT_INJECTION,
                    reason="Message contains potential prompt injection attempt",
                    matched_pattern=name,
                )

        return ValidationResult(is_safe=True, risk=SecurityRisk.NONE)

    def _check_pii(self, message: str) -> ValidationResult:
        """Check for PII patterns (GDPR compliance)."""
        for risk, (pattern, description) in self._pii_patterns.items():
            if pattern.search(message):
                return ValidationResult(
                    is_safe=False,
                    risk=risk,
                    reason=description,
                    redirect_to="support_api",
                    matched_pattern=risk.value,
                )

        return ValidationResult(is_safe=True, risk=SecurityRisk.NONE)

    def sanitize(self, message: str) -> str:
        """
        Sanitize a message by removing potentially dangerous content.

        Note: Use with caution. Prefer blocking over sanitizing for security.

        Args:
            message: Message to sanitize

        Returns:
            Sanitized message
        """
        sanitized = message

        # Remove format markers
        for pattern, _ in self._injection_patterns:
            sanitized = pattern.sub("", sanitized)

        return sanitized.strip()


# Singleton instance
_security_validator: Optional[SecurityValidator] = None


def get_security_validator() -> SecurityValidator:
    """Get or create security validator instance."""
    global _security_validator
    if _security_validator is None:
        _security_validator = SecurityValidator()
    return _security_validator
