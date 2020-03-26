import typer
from invoke import run, Context, Config
from .system import sum_paths
from ..utils.logs import logger


def exec(base_command, options='', exit_on_failure=True, tee=None, context=None):
    full_command = f'{base_command} {options}'
    if tee:
        full_command += f' | tee {tee}'
    # logger.debug(f'Executing command:\n{full_command}')

    if context:
        myrun = context.run
    else:
        myrun = run
    # print(myrun, full_command)
    # exit()
    result = myrun(full_command, shell='/bin/ash', hide=True, warn=True)
    # logger.debug(result)

    if result.ok:
        # logger.debug(result.stdout)
        pass
    else:
        logger.error(f'Shell error:\n{result.stderr}')
        if exit_on_failure:
            raise typer.Exit(1)
    return result.stdout.strip()


def exec_in_dir(base_command, directory, options='', tee=None, exit_on_failure=True):
    if tee:
        tee = sum_paths(directory, tee)

    # NOTE: Path doesn't seem to be compatible with cd here,
    # see PR https://j.mp/3dq3nvf
    directory = str(directory)

    config = Config()
    config.load_shell_env()
    context = Context(config=config)

    # with context.cd(str(directory)):
    with context.cd(directory):
        exec(base_command, options, exit_on_failure, tee=tee, context=context)
