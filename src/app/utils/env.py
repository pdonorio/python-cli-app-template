import typer
from glom import glom
from parse_it import ParseIt
from .logs import logger
from ..shell.system import etc_path, sum_paths


CONFIG_PATH = sum_paths(etc_path("app"), "config", return_string=True)


def setup():
    config_type_priority = [
        # 'cli_args',  # allow using typer
        "envvars",
        "env",
        "yml",
        "yaml",
        "json",
        "toml",
        "conf",
        "cfg",
        "ini",
    ]
    return ParseIt(
        config_location=CONFIG_PATH,
        recurse=True,
        config_type_priority=config_type_priority,
    )


PARSER = setup()


def read_all_configs(parser=None):
    if parser is None:
        parser = PARSER
    try:
        envs = parser.read_all_configuration_variables()
    except IndexError:
        logger.warning("Empty command line parameters: not allowed")
        raise typer.Exit()
    else:
        return envs


def get_var(key, parser=None, sep=".", **kwargs):
    if parser is None:
        parser = PARSER
    glomming = sep in key
    if glomming:
        default = kwargs.pop("default_value", None)
        value = glom(read_all_configs(), key, default=default)
    else:
        value = parser.read_configuration_variable(key, **kwargs)
    return value


# def get_group(prefix):
#     prefix = f'{prefix.lower()}_'
#     all_vars = read_all_configs()
#     return {
#         key.replace(prefix, ''): value
#         for key, value in all_vars.items()
#         if key.startswith(prefix)
#     }


def get_project_name():
    return get_var("project.name", default_value="my project").replace(" ", "_")
