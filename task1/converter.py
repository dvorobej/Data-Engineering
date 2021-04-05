# -*- coding: utf-8 -*-
"""
Version 1.1
@author: Dmitry Vorobey
"""

import pandas as pd
import pyarrow as pa
from command_parser import get_command_arguments


def convert_csv_to_parquet(csv_path, prq_path, debug_mode):
    """
    Converts the .csv file to the .parquet file and saves it.

        Params:
            csv_path (str): path to .csv file
            prq_path (str): path to .parquet file
            debug_mode (bool): flag to print the result of work

        Return value:
            None
    """
    try:
        input_csv = pd.read_csv(csv_path)
        try:
            input_csv.to_parquet(prq_path, index=False)
        except Exception as e:
            print(f"Could not convert the csv file to the parquet file:{prq_path}", e)
            return None
    except Exception as e:
        print(f"Could not read the csv file:{csv_path}", e)
        return None
    if debug_mode:
        print(f"CSV file {csv_path} was converted to parquet file {prq_path}")


def convert_parquet_to_csv(csv_path, prq_path, debug_mode):
    """
    Converts the .parquet file to the .csv file and saves it.

        Params:
            csv_path (str): path to .csv file
            prq_path (str): path to .parquet file
            debug_mode (bool): flag to print the result of work

        Return value:
            None
    """
    try:
        input_prq = pd.read_parquet(prq_path)
        try:
            input_prq.to_csv(csv_path, index=False)
        except Exception as e:
            print(f"Could not convert the parquet file to the csv file:{csv_path}", e)
            return None
    except Exception as e:
        print(f"Could not read the parquet file:{prq_path}", e)
        return None
    if debug_mode:
        print(f"Parquet file {prq_path} was converted to csv file {csv_path}")


def get_parquet_schema(prq_path):
    """
    Get the shema of the parquet file on the command line.

        Params:
            prq_path (str): path to the printed .parquet file

        Return value:
            schema_df (pandas.core.frame.DataFrame): schema of the .parquet file
    """
    try:
        input_prq = pd.read_parquet(prq_path)
        schema_df = pd.DataFrame(
            {
                "column_name": pa.Schema.from_pandas(input_prq).names,
                "column_type": pa.Schema.from_pandas(input_prq).types,
            }
        )
        return schema_df
    except Exception as e:
        print(f"Could not read the parquet file:{prq_path}", e)
        return None


def main():
    """
    Depending on the command line arguments: converts the .csv file to the .parquet file|
    converts the .parquet file to the .csv file| prints the schema of parquet file.

        Return value:
            None
    """
    command_args = get_command_arguments()

    # Delete possible quotes in paths
    input_file_path = command_args.infile.strip("'\"")
    output_file_path = command_args.outfile.strip("'\"")

    if command_args.prq_to_csv:
        convert_parquet_to_csv(
            csv_path=output_file_path,
            prq_path=input_file_path,
            debug_mode=command_args.debug,
        )
    elif command_args.csv_to_prq:
        convert_csv_to_parquet(
            csv_path=input_file_path,
            prq_path=output_file_path,
            debug_mode=command_args.debug,
        )
    elif command_args.schema:
        schema_df = get_parquet_schema(prq_path=input_file_path)
        print(schema_df)
    else:
        print("Problem with required arguments occured")


if __name__ == "__main__":
    main()
