from pathlib import Path

from pandas import DataFrame

from __config__ import PROJECT_SOURCE_PATH


def write_csv(absolute_path: str, obj: DataFrame) -> None:
    """
    :param absolute_path: Absolute path for input file
    :param obj: DataFrame obj with data
    :return: DataFrame object of input file data

    Function, that writes *.csv files
    """

    print(f"    Writing to {absolute_path}")
    obj.to_csv(absolute_path, encoding='utf8')
    print(f"    End of data writing")


def write_xlsx(absolute_path: str, obj: DataFrame) -> None:
    """
    :param absolute_path: Absolute path for input file
    :param obj: DataFrame obj with data
    :return: DataFrame object of input file data

    Function, that writes *.xlsx files
    """

    print(f"    Writing to {absolute_path}")
    obj.to_excel(absolute_path)
    print(f"    End of data writing")


def write_middleware(file_name: str, dataset: DataFrame) -> None:
    """
    :param dataset: DataFrame obj with data
    :param file_name: relative file path
    :return: Array of input file data

    Function, that choose write function according to the file type
    """

    write_func: dict = {
        'csv': write_csv,
        'xlsx': write_xlsx
    }

    file_type: str = file_name.split('.')[-1]
    absolute_path: Path = Path(f'{PROJECT_SOURCE_PATH}\\{file_type}\\{file_name}')

    func = write_func.get(file_type)
    if not func:
        raise ValueError(
            f'Unknown file type "{file_type}" '
            f'(file types must be one of ({", ".join(f".{key}" for key in write_func.keys())})'
        )
    func(absolute_path, dataset)
