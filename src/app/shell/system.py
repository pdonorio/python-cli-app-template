import re
import os
from pathlib import Path
from .. import ROOT_PATH, PACKAGE_PATH


def set_env_var(key, value):
    os.environ[key] = value


def root_path():
    return Path(os.path.abspath(os.sep))


def sum_paths(base, suffix, return_string=False):
    path = base.joinpath(suffix)
    if return_string:
        path = str(path)
    return path


def etc_path(relative_dir=None):
    etc_path = root_path() / "etc"
    if relative_dir:
        return etc_path.joinpath(relative_dir)
    return etc_path


def lib_path(relative_dir=None):
    lib_path = root_path() / "usr" / "lib"
    if relative_dir:
        return lib_path.joinpath(relative_dir)
    return lib_path


def relative_path(steps):
    path = Path()
    for step in steps:
        path = path.joinpath(step)
    return path


def path_relative_to_package(relative_path):
    return Path(PACKAGE_PATH).joinpath(relative_path)


def path_relative_to_app(relative_path):
    return Path(ROOT_PATH).joinpath(relative_path)


def read_content(file_path):
    with open(file_path) as f:
        return f.read()


def find_in_logs(log_file_path, after=None, before=None):
    content = read_content(log_file_path)
    if after:
        tmp = re.split(after, content)
        if len(tmp) < 2:
            return
        content = tmp[1]
    if before:
        tmp = re.split(before, content)
        if len(tmp) < 2:
            return
        content = tmp[0]
    return content
