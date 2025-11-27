# job-intelligence-platform

## Setup

1. Copy `backend/alembic.ini.example` to `backend/alembic.ini`
2. Update database credentials in `alembic.ini`
3. Run `docker-compose up -d` to start PostgreSQL
4. Run migrations: `alembic upgrade head`