import typer
from .app import settings

app = typer.Typer()


@app.command()
def test1(parameter: int = 1):
    ''' bla bla '''
    typer.echo(parameter)


@app.command()
def test2():
    ''' bla bla '''
    typer.echo(settings.all)
