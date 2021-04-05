# -*- coding: utf-8 -*-
"""
Version 1.1

@author: Dmitry Vorobey
"""

import argparse


def get_command_arguments():
    """
    Get the arguments from the command line.

        Return value:
            command_args (argparse.Namespace): arguments of the command line
    """

    parser = argparse.ArgumentParser()

    parser.add_argument("-N", type=int, help="number of films to show")
    parser.add_argument("-g", "--genres", type=str, help="filter by genres")
    parser.add_argument("-year_from", type=int, help="year lower bound filter")
    parser.add_argument("-year_to", type=int, help="year upper bound filter")
    parser.add_argument("-regexp", type=str, help="name of the film filter")

    command_args = parser.parse_args()

    return command_args
