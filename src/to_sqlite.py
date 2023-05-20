import json
import sqlite3
import pandas as pd


def read_stg_json(filename: str) -> pd.DataFrame:
    with open(filename, "r") as jf:
        raw_data = json.load(jf)
    actual_data = raw_data["result"]["records"]
    return pd.DataFrame(actual_data)


def write_to_sqlite(df: pd.DataFrame, table_name: str) -> None:
    with sqlite3.Connection("data/final.db") as con:
        df.to_sql(table_name, con, if_exists="append")


def main():
    tabular_data = read_stg_json("data/oci.json")
    write_to_sqlite(tabular_data, "MAIN_TABLE")


if __name__ == "__main__":
    main()
