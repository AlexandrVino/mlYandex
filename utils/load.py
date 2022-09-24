import logging
from pathlib import Path

from pandas import DataFrame, read_csv, read_excel

from __config__ import PROJECT_SOURCE_PATH

log = logging.getLogger(__name__)


def load_csv(absolute_path: str) -> DataFrame:
    """
    :param absolute_path: Absolute path for input file
    :return: DataFrame object of input file data

    Function, that loads *.csv files
    """

    log.info(f"Loading %s" % absolute_path)
    return read_csv(absolute_path)


def load_xlsx(absolute_path: str) -> DataFrame:
    """
    :param absolute_path: Absolute path for input file
    :return: DataFrame object of input file data

    Function, that loads *.xlsx files
    """

    log.info(f"Loading %s" % absolute_path)
    return read_excel(absolute_path)


def load_middleware(file_name: str) -> DataFrame:
    """
    :param file_name: relative file path
    :return: Array of input file data

    Function, that choose upload function according to the file type
    """

    read_func: dict = {
        'csv': load_csv,
        'xlsx': load_xlsx,
    }

    file_type: str = file_name.split('.')[-1]

    absolute_path: Path = Path(f'{PROJECT_SOURCE_PATH}\\{file_type}\\{file_name}')

    func = read_func.get(file_type)
    if not func:
        raise ValueError(
            f'Unknown file type "{file_type}" '
            f'(file types must be one of ({", ".join(f".{key}" for key in read_func.keys())})'
        )

    val = func(absolute_path)
    log.info(f"End of data loading")

    return val
