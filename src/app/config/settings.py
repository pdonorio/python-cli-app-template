import typer
from dataclasses import dataclass
from . import ConfigWrapper
from ..utils import env

app = typer.Typer()


@dataclass
class Settings:
    project_name: str = env.get_project_name()
    verbose: bool = False
    all: dict = None


settings = Settings()
cfg = env.read_all_configs()
settings.all = ConfigWrapper(cfg)
