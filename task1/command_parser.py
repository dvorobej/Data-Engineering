# -*- coding: utf-8 -*-
"""
Version 1.0

@author: Dmitry Vorobey
"""

import argparse


def get_command_arguments():
    """
    Gets the arguments from the command line.

        Return value:
            command_args (argparse.Namespace): arguments of the command line
    """
    parser = argparse.ArgumentParser()

    # Mutually exclusive argument defining the main logic of the program
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-tocsv",
        "--prq_to_csv",
        action="store_true",
        help="convert .parquet file to .csv file",
    )
    group.add_argument(
        "-toprq",
        "--csv_to_prq",
        action="store_true",
        help="convert .csv file to .parquet file",
    )
    group.add_argument(
        "-s", "--schema", action="store_true", help="print .parquet file schema"
    )

    parser.add_argument(
        "-i", "--infile", required=True, type=str, help="input file path"
    )
    parser.add_argument(
        "-o", "--outfile", default="./output", type=str, help="output file path"
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="shows the results of work"
    )

    command_args = parser.parse_args()

    return command_args
