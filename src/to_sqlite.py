import json
import os
import sqlite3
import pandas as pd

from . import utils


def read_stg_json(filename: str) -> pd.DataFrame:
    """Reads the json in filename path. Returns it as a tabular DataFrame.
    The json must have result and records section.
    """
    with open(filename, "r") as jf:
        raw_data = json.load(jf)
    actual_data = raw_data["result"]["records"]

    return pd.DataFrame(actual_data)


def write_to_sqlite(dest: str, df: pd.DataFrame, table_name: str) -> None:
    """Write df data to table_name in dest database."""
    with sqlite3.Connection(dest) as con:
        df.to_sql(table_name, con, if_exists="append")


def main(args):
    src_file = os.path.join(args.data_root, utils.generate_daily_filename())
    tabular_data = read_stg_json(src_file)

    destination = os.path.join(args.data_root, args.final_db)
    write_to_sqlite(destination, tabular_data, args.main_table)


if __name__ == "__main__":
    args = utils.args_from_config("config.ini")
    main(args)
