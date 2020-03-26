from . import sub
from .app import app  # , settings

# import typer


app.add_typer(sub.app, name='sub', help='Subcommand example')


@app.command()
def normal(mybool: bool = False):
    ''' Normal command example '''
    pass
