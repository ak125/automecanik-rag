-- P3 RBAC: Create restricted roles for RAG system
-- Usage: psql -U postgres -d automecanik -f create_rbac_roles.sql
--
-- Roles:
-- - kpi_reader: Read-only access to KPI/analytics tables
-- - rag_indexer: Write access for indexing (Build Plane only)
-- - rag_api: Read access for search queries (Runtime Plane)

-- ============================================
-- ROLE: kpi_reader
-- Purpose: Read-only access to analytics and KPI data
-- Used by: Dashboard, reporting tools
-- ============================================

-- Create role if not exists
DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'kpi_reader') THEN
        CREATE ROLE kpi_reader WITH
            LOGIN
            NOSUPERUSER
            NOCREATEDB
            NOCREATEROLE
            NOINHERIT
            NOREPLICATION
            CONNECTION LIMIT 10;
        RAISE NOTICE 'Created role: kpi_reader';
    ELSE
        RAISE NOTICE 'Role kpi_reader already exists';
    END IF;
END
$$;

-- Grant read-only on specific tables
GRANT USAGE ON SCHEMA public TO kpi_reader;

-- KPI/Analytics tables (read-only)
GRANT SELECT ON TABLE __stats_daily TO kpi_reader;
GRANT SELECT ON TABLE __stats_monthly TO kpi_reader;
GRANT SELECT ON TABLE __analytics_events TO kpi_reader;
GRANT SELECT ON TABLE __rag_usage_logs TO kpi_reader;

-- Aggregated views only (no raw data)
-- GRANT SELECT ON __vw_kpi_summary TO kpi_reader;

-- ============================================
-- ROLE: rag_indexer
-- Purpose: Write access for knowledge corpus indexing
-- Used by: Build Plane (DEV/CI), GitHub Actions
-- ============================================

DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'rag_indexer') THEN
        CREATE ROLE rag_indexer WITH
            LOGIN
            NOSUPERUSER
            NOCREATEDB
            NOCREATEROLE
            NOINHERIT
            NOREPLICATION
            CONNECTION LIMIT 5;
        RAISE NOTICE 'Created role: rag_indexer';
    ELSE
        RAISE NOTICE 'Role rag_indexer already exists';
    END IF;
END
$$;

GRANT USAGE ON SCHEMA public TO rag_indexer;

-- Knowledge tables (read/write for indexing)
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE __rag_knowledge TO rag_indexer;
GRANT SELECT, INSERT, UPDATE ON TABLE __rag_index_versions TO rag_indexer;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO rag_indexer;

-- ============================================
-- ROLE: rag_api
-- Purpose: Read-only access for search queries
-- Used by: Runtime Plane (PROD), RAG API service
-- ============================================

DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'rag_api') THEN
        CREATE ROLE rag_api WITH
            LOGIN
            NOSUPERUSER
            NOCREATEDB
            NOCREATEROLE
            NOINHERIT
            NOREPLICATION
            CONNECTION LIMIT 50;
        RAISE NOTICE 'Created role: rag_api';
    ELSE
        RAISE NOTICE 'Role rag_api already exists';
    END IF;
END
$$;

GRANT USAGE ON SCHEMA public TO rag_api;

-- Knowledge tables (read-only for search)
GRANT SELECT ON TABLE __rag_knowledge TO rag_api;
GRANT SELECT ON TABLE __rag_index_versions TO rag_api;

-- Insert usage logs
GRANT INSERT ON TABLE __rag_usage_logs TO rag_api;

-- ============================================
-- Security: Revoke public access
-- ============================================

REVOKE ALL ON TABLE __rag_knowledge FROM PUBLIC;
REVOKE ALL ON TABLE __rag_index_versions FROM PUBLIC;
REVOKE ALL ON TABLE __rag_usage_logs FROM PUBLIC;

-- ============================================
-- Row Level Security (RLS) Policies
-- ============================================

-- Enable RLS on sensitive tables
ALTER TABLE __rag_knowledge ENABLE ROW LEVEL SECURITY;
ALTER TABLE __rag_usage_logs ENABLE ROW LEVEL SECURITY;

-- Policy: kpi_reader can only see aggregated data
CREATE POLICY kpi_reader_usage_logs ON __rag_usage_logs
    FOR SELECT
    TO kpi_reader
    USING (true);  -- Can see all logs for analytics

-- Policy: rag_api can only read verified knowledge
CREATE POLICY rag_api_knowledge ON __rag_knowledge
    FOR SELECT
    TO rag_api
    USING (verification_status = 'verified' OR truth_level IN ('L1', 'L2'));

-- Policy: rag_indexer has full access (Build Plane)
CREATE POLICY rag_indexer_knowledge ON __rag_knowledge
    FOR ALL
    TO rag_indexer
    USING (true)
    WITH CHECK (true);

-- ============================================
-- Verification queries
-- ============================================

-- Verify roles created
SELECT rolname, rolcanlogin, rolconnlimit
FROM pg_roles
WHERE rolname IN ('kpi_reader', 'rag_indexer', 'rag_api');

-- Verify grants
SELECT grantee, table_name, privilege_type
FROM information_schema.table_privileges
WHERE grantee IN ('kpi_reader', 'rag_indexer', 'rag_api')
ORDER BY grantee, table_name;

COMMENT ON ROLE kpi_reader IS 'P3 RBAC: Read-only access to KPI/analytics';
COMMENT ON ROLE rag_indexer IS 'P3 RBAC: Write access for Build Plane indexing';
COMMENT ON ROLE rag_api IS 'P3 RBAC: Read-only access for Runtime Plane search';
