import importlib


def get_module_from_path(module_path):
    return importlib.import_module(module_path)


def get_function_in_module(module_path, function_name):
    module = get_module_from_path(module_path)
    return getattr(module, function_name)
