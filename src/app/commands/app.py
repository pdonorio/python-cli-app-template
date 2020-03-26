import typer
from ..config.settings import settings
from ..utils.logs import reset_level, logger

app = typer.Typer()


@app.callback()  # invoke_without_command=True)
def init(ctx: typer.Context, verbose: bool = False, project_name: str = None):
    """
    *Awesome* command line app
    """

    # NOTE: define logs level, as first thing
    settings.verbose = verbose
    reset_level(verbose=verbose)

    if project_name:
        settings.project_name = project_name

    logger.info(f'Project: {settings.project_name}')
    logger.debug(f'Command: {ctx.invoked_subcommand}')
    if settings.verbose:
        logger.debug(f'Verbose is ON')
