# python-cli-app-template

A template to have a working cli app in 10 seconds.

## what

Batteries included:
- logs
- commands and subcommands, usage
- configuration file and env variables
- setup for packaging
- system commands / shell handling
- docker image template
- docker compose template

## how

```bash
# setup
docker-compose build
docker-compose up -d
docker-compose exec app zsh

# inside the container
pip install -e .

# some examples
myapp --help
myapp normal
myapp sub
myapp --verbose sub test1 --parameter 5
myapp sub test1 --parameter test
exit

# the end
docker-compose down --remove-orphans --volumes --rmi all
```

NOTE: if you use Sublime Text, please consider using the [`black` formatter](https://black.readthedocs.io/) through the [sublack](https://github.com/jgirardet/sublack#table-of-content) plugin (which runs it 'on save').
