from pathlib import Path
from .run import exec as shell


def set_symbolic(src, dest, force=False):
    if not Path(src).exists():
        return
    symbolic = '-s'
    if force:
        symbolic += 'f'
    return shell(f'ln {symbolic} {src} {dest}')
