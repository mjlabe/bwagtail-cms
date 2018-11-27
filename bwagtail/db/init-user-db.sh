#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER wagtail with password 'wagtail';
    CREATE DATABASE wagtail;
    GRANT ALL PRIVILEGES ON DATABASE wagtail TO wagtail;
EOSQL
