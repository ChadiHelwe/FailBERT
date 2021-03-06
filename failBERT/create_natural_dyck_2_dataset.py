#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = Chadi Helwe 
__version__ = 1.0
__maintainer__ = Chadi Helwe
__email__ = chadi.helwe@telecom-paris.fr
__description__ = Module to create the dataset of natural dyck-2 task
"""

import csv
import random
from typing import List, Optional, Tuple


def convert_dyck_2_to_natural_instance(dyck_2: str) -> Tuple[List[str], List[str]]:
    """
    Convert a dyck-2 instance to a natural dyck-2 instance

    :param dyck_2: Dyck-2 instance
    :type dyck_2: str
    :return: List of dyck-2 natural tokens and list of dyck-2 symbols tokens
    :rtype: Tuple[List[str], List[str]]
    """

    symbols_to_instance = {
        "[": "I added a peanut layer to my cake",
        "(": "I added a chocolate layer to my cake",
        "]": "I ate the peanut layer",
        ")": "I ate the chocolate layer",
    }

    list_str_dyck = []
    list_str_dyck_symbols = []
    for s in dyck_2:
        list_str_dyck.append(f"{symbols_to_instance[s]}")
        list_str_dyck_symbols.append(f"{s}: {symbols_to_instance[s]}")

    return list_str_dyck, list_str_dyck_symbols


def convert_to_swapped_false_instance(
    list_str_dyck: List[str], list_str_dyck_symbols: List[str]
) -> Tuple[List[str], List[str], Optional[int], bool]:
    """
    Create a negative natural dyck-2 instance from a postive natural dyck-2 instance

    :param list_str_dyck: List of dyck-2 natural tokens
    :type list_str_dyck: List[str]
    :param list_str_dyck_symbols: List of dyck-2 symbols tokens
    :type list_str_dyck_symbols: List[str]
    :return: Negative list of natural dyck-2 token, negative list of dyck-2 symbols tokens, swapped index, and label of the instance
    :rtype: Tuple[List[str], List[str], Optional[int], bool]
    """

    peanut_indexes = [
        i for i, s in enumerate(list_str_dyck) if s == "I ate the peanut layer"
    ]
    chocolate_indexes = [
        i for i, s in enumerate(list_str_dyck) if s == "I ate the chocolate layer"
    ]

    label = True
    index = None

    if len(peanut_indexes) > 0 and len(chocolate_indexes) > 0:
        index_1 = random.choice(peanut_indexes)
        index_2 = random.choice(chocolate_indexes)

        list_str_dyck[index_1], list_str_dyck[index_2] = (
            list_str_dyck[index_2],
            list_str_dyck[index_1],
        )
        list_str_dyck_symbols[index_1], list_str_dyck_symbols[index_2] = (
            list_str_dyck_symbols[index_2],
            list_str_dyck_symbols[index_1],
        )

        label = False
        index = (index_1, index_2)

    return list_str_dyck, list_str_dyck_symbols, index, label


def to_str(list_str_dyck: List[str]) -> str:
    """
    Convert a list of natural dyck-2 token to a string

    :param list_str_dyck: List of dyck-2 natural tokens
    :type list_str_dyck: List[str]
    :return: Natural dyck-2 string
    :rtype: str
    """

    str_dyck = " , ".join(list_str_dyck[:-1])
    str_dyck += f" and {list_str_dyck[-1]} ."
    return str_dyck


def create_dataset(path_dyck_2_dataset: str, path_natural_dyck_2_dataset: str) -> None:
    """
    Create a natural dyck-2 dataset

    :param path_dyck_2_dataset: Path of the dyck-2 dataset
    :type path_dyck_2_dataset: str
    :param path_natural_dyck_2_dataset: Path to save the natural dyck-2 dataset
    :type path_natural_dyck_2_dataset: str
    """

    with open(path_natural_dyck_2_dataset, "w") as dataset:
        dataset_writer = csv.writer(dataset)
        dataset_writer.writerow(
            [
                "modified_sentence",
                "modified_sentence_with_symbols",
                "dyck_format",
                "index",
                "label",
            ]
        )
        with open(path_dyck_2_dataset, "r") as f:

            for l in f.readlines():
                (
                    list_str_dyck,
                    list_str_dyck_symbols,
                ) = convert_dyck_2_to_natural_instance(l.strip())
                dataset_writer.writerow(
                    [
                        to_str(list_str_dyck),
                        to_str(list_str_dyck_symbols),
                        l.strip(),
                        str(None),
                        True,
                    ]
                )
                (
                    false_list_str_dyck,
                    false_list_str_dyck_symbols,
                    index,
                    label,
                ) = convert_to_swapped_false_instance(
                    list_str_dyck, list_str_dyck_symbols
                )
                if not label:
                    dataset_writer.writerow(
                        [
                            to_str(false_list_str_dyck),
                            to_str(false_list_str_dyck_symbols),
                            l.strip(),
                            index,
                            label,
                        ]
                    )
