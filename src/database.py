from advanced_alchemy.extensions.litestar import (
    AsyncSessionConfig, SQLAlchemyAsyncConfig, SQLAlchemyInitPlugin
)

from src.config import AppConfig as ac

sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=f'postgresql+asyncpg://{ac.pg_user}:{ac.pg_pass}@{ac.pg_host}:{ac.pg_port}/{ac.pg_db}',
    session_config=AsyncSessionConfig(expire_on_commit=False)
)
sqlalchemy_plugin = SQLAlchemyInitPlugin(config=sqlalchemy_config)
