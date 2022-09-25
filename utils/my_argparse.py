import os
from argparse import ArgumentTypeError, Namespace
from typing import Callable

ENV_VAR_PREFIX = 'ml_yandex_'


def setup_basic_config() -> Namespace:
    """
    :return: Namespace obj with parameters of running file

    Function, that setups logs, clear parameters from .env file
    """

    clear_environ(lambda arg: arg.startswith(ENV_VAR_PREFIX))

    return Namespace(input_from='datasets_eat_places.csv')


def validate(arg_type: Callable, constrain: Callable) -> Callable:
    """
    :param arg_type: type for that must convert value
    :param constrain:
    :return: Filter function

    Function that create filters
    (For example: positive_int = validate(int, constrain=lambda x: x > 0))
    """

    def wrapper(value):
        value = arg_type(value)
        if not constrain(value):
            raise ArgumentTypeError
        return value

    return wrapper


def clear_environ(rule: Callable):
    """
    :param rule: the rule for clean .env variables
    :return:

    Function that clears environment variables, the variables to be cleaned are determined by the passed
    the rule function.
    """

    # Ключи из os.environ копируются в новый tuple, чтобы не менять объект
    # os.environ во время итерации.
    for name in filter(rule, tuple(os.environ)):
        os.environ.pop(name)
