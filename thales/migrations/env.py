from alembic import context
from prettyconf import config
from sqlalchemy import create_engine
from thales import db


DATABASE_URL = config('DATABASE_URL')
METADATA = db.metadata


def run_migrations_offline():
    context.configure(url=DATABASE_URL, metadata=METADATA)
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        context.configure(connection=connection, target_metadata=METADATA)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
