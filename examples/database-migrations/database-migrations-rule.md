# Database Migrations - Windsurf Rule

<!-- 
This is a Windsurf rule for database migrations.
To add this to Windsurf:
1. Click Customizations icon (top right in Cascade)
2. Navigate to Rules panel
3. Click "+ Workspace" button
4. Copy/paste this content
5. Set Activation Mode: "Always On"
6. Save
-->

## Critical Migration Rules

<database_migrations>

### ❌ NEVER Use Alembic
- This project uses **custom SQL migrations**, NOT Alembic
- NEVER run: `alembic upgrade head` 
- NEVER create: `alembic.ini`, `alembic/env.py`, or `alembic/versions/` files
- If you see Alembic files, DELETE them immediately

### ✅ ALWAYS Use Custom SQL Migration System
- Migration files: SQL only, located in `backend/migrations/` 
- Naming format: `NNN_descriptive_name.sql` (e.g., `040_add_notifications.sql`)
- Migration runner: `python scripts/run_migrations.py` 
- Database: Supabase PostgreSQL with pooler (port 6543)

### Before Creating Any Migration

1. **Check current status:**
   ```bash
   cd backend
   python scripts/run_migrations.py status
   ```

2. **Review existing migrations:**
   - List files in `backend/migrations/` 
   - Check what tables already exist
   - Verify migration number sequence

3. **Check table dependencies:**
   - Users table exists (migration 001)
   - Calendar_events created in migration 016
   - Don't reference tables that don't exist yet

### Creating a New Migration

**File Structure:**
```sql
-- Migration: NNN_description
-- Description: What this does
-- Date: YYYY-MM-DD
-- Depends on: Previous migrations

-- Use IF NOT EXISTS
CREATE TABLE IF NOT EXISTS your_table (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    created_at TIMESTAMPTZ DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT NOW() NOT NULL
);

-- Always add indexes for FKs
CREATE INDEX idx_your_table_user ON your_table(user_id);

-- Add triggers if needed
CREATE TRIGGER trigger_your_table_updated_at
    BEFORE UPDATE ON your_table
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();
```

### Running Migrations

**Standard workflow:**
```bash
# 1. Check status
python scripts/run_migrations.py status

# 2. Run all pending migrations
python scripts/run_migrations.py migrate

# 3. Or run up to specific number
python scripts/run_migrations.py migrate --upto 40

# 4. Verify success
python check_migrations.py
```

### Common Pitfalls to Avoid

1. **Foreign Key to Non-Existent Table:**
   - Check if referenced table exists in earlier migration
   - If not, create without FK constraint or add FK in later migration
   - Example: Don't reference `calendar_events` before migration 016

2. **Table Already Exists:**
   - Always use `CREATE TABLE IF NOT EXISTS` 
   - Check `python scripts/run_migrations.py status` first

3. **Wrong Database Driver:**
   - Use psycopg2 (NOT asyncpg) for migrations
   - Connection string should NOT include `+asyncpg` or `+psycopg` 

4. **Migration Fails Midway:**
   - Check error in output
   - Fix SQL file
   - Re-run: `python scripts/run_migrations.py migrate` 
   - Migration marked as failed in `schema_migrations` table

### Database Connection Details

**Environment Variables (from `.env`):**
- `DATABASE_URL`: Supabase connection string
- Format: `postgresql://user:pass@host:6543/postgres` 
- Pooler: Transaction mode (prepared statements disabled)
- Special config for Supabase compatibility

**Connection:**
- Provider: Supabase PostgreSQL
- Port: 6543 (pooler, not 5432)
- Driver: psycopg2
- Schema: public

### Verification Steps

**After running migration:**

1. **Check migration tracking:**
   ```bash
   python check_migrations.py
   ```

2. **Verify in Supabase:**
   - Go to https://supabase.com
   - Open project → Table Editor
   - Check tables exist

3. **SQL verification:**
   ```sql
   SELECT * FROM schema_migrations
   WHERE migration_name = 'NNN_your_migration';
   ```

### Migration Tracking System

**All migrations tracked in:**
```sql
schema_migrations (
    id SERIAL PRIMARY KEY,
    migration_name VARCHAR(255) UNIQUE,
    applied_at TIMESTAMPTZ,
    execution_time_ms INTEGER,
    success BOOLEAN
)
```

**Check applied migrations:**
```sql
SELECT migration_name, applied_at, success
FROM schema_migrations
ORDER BY applied_at DESC;
```

### Emergency Procedures

**If migration fails:**
1. Don't panic - check error message
2. Run: `python scripts/run_migrations.py status` 
3. Fix the SQL file
4. Re-run: `python scripts/run_migrations.py migrate` 

**If database is inconsistent:**
1. Check tables: `python check_migrations.py` 
2. Connect to Supabase SQL Editor
3. Run corrective SQL manually
4. Mark migration as applied if needed

### Best Practices Checklist

**Before creating:**
- [ ] Checked existing migrations
- [ ] Verified next sequential number
- [ ] Confirmed table dependencies
- [ ] Used descriptive filename

**In SQL file:**
- [ ] Include header comments
- [ ] Use `IF NOT EXISTS` 
- [ ] Add indexes for foreign keys
- [ ] Include `created_at`, `updated_at` timestamps
- [ ] Add triggers for `updated_at` 
- [ ] Use `uuid_generate_v4()` for UUIDs

**After running:**
- [ ] Verified with `check_migrations.py` 
- [ ] Checked Supabase dashboard
- [ ] Confirmed in `schema_migrations` table
- [ ] Committed SQL file to git

### Reference Documentation

**Detailed guides:**
- Complete guide: `docs/AI_AGENT_RULES_DATABASE_MIGRATIONS.md` 
- Quick reference: `MIGRATIONS_QUICK_REFERENCE.md` 
- Auth setup: `docs/BACKEND_AUTH_SETUP_COMPLETE.md` 

**Key files:**
- Migration runner: `backend/scripts/run_migrations.py` 
- Migrations: `backend/migrations/*.sql` 
- Verification: `backend/check_migrations.py` 

### Examples of Existing Migrations

**Users & Auth (001):**
- Creates: users, permissions, teams, roles
- Sets up RBAC system
- Includes default admin user

**Google Calendar (039):**
- Creates: google_calendar_connections
- Creates: calendar_event_sync_map
- Creates: google_calendar_sync_log
- Note: No FK to calendar_events (doesn't exist yet)

</database_migrations>

## Summary

When working with database migrations:
1. **NEVER** use Alembic
2. **ALWAYS** use `python scripts/run_migrations.py` 
3. **CHECK** status before creating new migrations
4. **VERIFY** with `python check_migrations.py` 
5. **READ** detailed docs if unsure

**Success rate following these rules: 100%**
