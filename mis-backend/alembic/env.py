#DB migration scripts
import asyncio
from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config
from alembic import context
import os
from dotenv import load_dotenv

#load .env file
load_dotenv()

#Alembic config object
config = context.config

#set sqlalchemy.url from .env file
config.set_main_option("sqlalchemy.url"
os.getenv("DATABASE_URL"))

#Interpret the config file for python Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

#Import models
#Replace 'app.core.database' with actual path with Base
from app.core.database import Base
target_metadata = Base.metadata

def run_migrations_offline():
    """Run migration offline"""
    url = config.get_main_option("sqlalchemy.url")
    context.config(
        url = url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle":"pyformat"},
    )

    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection):
    context.configure(connection=connection,
target_metadata=target_metadata)
    
    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online():
    """Run migration online"""
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()

if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())