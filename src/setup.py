from setuptools import setup

install_requires = ['typer', 'loguru', 'parse_it', 'glom', 'invoke']
app_location = 'app.__main__:app'

setup(
    name='Python App template',
    version='0.0.1',
    author='...',
    author_email='...@example.com',
    packages=['app'],
    install_requires=install_requires,
    entry_points={'console_scripts': [f'myapp={app_location}']},
)
