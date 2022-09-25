import logging
import math
import numpy as np
from pandas import DataFrame, Series

from utils.load import load_middleware
from utils.my_argparse import setup_basic_config

log = logging.getLogger(__name__)


def point_two(dataset: DataFrame) -> DataFrame:
    """
    :param dataset: DataFrame obj of table
    :return:
    """

    # Showing info about non-null values
    # (To see missed values (43195-non-null) values)
    log.info(dataset.info(show_counts=True))
    log.info('\n\n\n')

    # Drop rows from the DataFrame, where average_bill is null or more than 2500
    dataset_with_filter = dataset.query(
        'average_bill != None and average_bill <= 2500'
    )

    # fill in the remaining gaps with average values
    return dataset_with_filter.fillna(dataset_with_filter.mean(numeric_only=True))


def point_three(dataset: DataFrame) -> None:
    """
    :param dataset: DataFrame obj of table
    :return:
    """

    # Showing counts of coffee shops in sbp and msk
    log.info(f'\n{dataset["city"].value_counts()}\n')
    # Showing types of coffee shops
    # (I'm sorting it by len because I like it)
    sep = '\n'
    coffee_shop_types = sorted(
        set(dataset["rubric"].tolist()),
        key=lambda x: len(x)
    )
    log.info(f'\n{sep.join(coffee_shop_types)}\n')

    keys = {'Ресторан', 'Бар, паб'}
    rests_and_pubs = dataset.query(
        f'rubric in {tuple(keys)}'
    )

    vals = rests_and_pubs["rubric"].value_counts()
    counts = sum(vals[key] for key in keys)

    rests_and_pubs_values = rests_and_pubs.agg(
        {"average_bill": "sum"}
    ).reset_index()

    # getting average bill
    average_bill = rests_and_pubs_values[0][0] / counts

    log.info(f'\nAverage Bill: {average_bill}\n')


def main():
    # Getting arguments from command line
    args = setup_basic_config()

    # Getting values from table
    dataset: DataFrame = load_middleware(args.input_from)

    # Point Two
    dataset = point_two(dataset)

    # Point Three
    point_three(dataset)


if __name__ == '__main__':
    main()
