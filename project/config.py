import os
import pathlib
from functools import lru_cache


class BasicConfig:
    BASE_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent

    DATABASE_URL: str = os.environ.get("DATABASE_URL", f"sqlite:///{BASE_DIR}/db.sqlite3")
    DATABASE_CONNECT_DICT: dict = {}


class DevelopmentConfig(BasicConfig):
    pass


class ProductionConfig(BasicConfig):
    pass


class TestingConfig(BasicConfig):
    pass


@lru_cache()
def get_settings():
    config_cls_dict = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig
    }

    config_name = os.environ.get('FASTAPI_CONFIG', 'development')
    config_cls = config_cls_dict[config_name]
    return config_cls()


settings = get_settings()
