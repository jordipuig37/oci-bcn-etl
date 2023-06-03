import json
import os
import re
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
        df.to_sql(table_name, con, index=False, if_exists="append")


renamer = {
    'register_id': None,
    'name': None,
    'institution_id': None,
    'institution_name': None,
    'created': None,
    'modified': None,
    'addresses_roadtype_id': None,
    'addresses_roadtype_name': "Roadtype_name",
    'addresses_road_id': None,
    'addresses_road_name': "Road_name",
    'addresses_start_street_number': "Street_number",
    'addresses_end_street_number': None,
    'addresses_neighborhood_id': None,
    'addresses_neighborhood_name': "Neighborhood",
    'addresses_district_id': None,
    'addresses_district_name': None,
    'addresses_zip_code': None,
    'addresses_town': None,
    'addresses_main_address': None,
    'addresses_type': None,
    'geo_epgs_4326_x': "Longitude",
    'geo_epgs_4326_y': "Latitude",
    'values_category': None,
    'values_attribute_name': None,
    'values_value': "Telephone",
    'values_description': None
}


@utils.use_copy
def transform_rename(inp_df: pd.DataFrame) -> pd.DataFrame:
    out_df = inp_df.rename(columns={k: v for k, v in renamer.items() if v is not None})

    return out_df


def transform_filter_nulls(inp_df: pd.DataFrame) -> pd.DataFrame:
    """Filter rows with null in some key fields."""

    return inp_df[inp_df.isna().sum(axis=1).apply(lambda x: x < 10)]


def standarize_telephone(tel: str) -> int:
    """Standarize telephone numbers by removing all non-numeric characters from
    the input. Return the integer.
    """
    only_numbers = re.sub(r"\D", "", tel)
    try:
        return int(only_numbers)
    except ValueError:  # something bad happened
        return -1
    except BaseException as e:
        raise e


@utils.use_copy
def transform_telephone(inp_df: pd.DataFrame) -> pd.DataFrame:
    inp_df["Telephone"] = inp_df["Telephone"].apply(standarize_telephone)

    return inp_df


@utils.use_copy
def main_transformation(inp_df: pd.DataFrame) -> pd.DataFrame:
    """Apply all the transformations to the input dataframe.
    Return a new dataframe with the processed data.
    """
    out_df = transform_filter_nulls(inp_df)
    out_df = out_df[list(renamer.keys())]  # select fields
    out_df = transform_rename(out_df)
    out_df = transform_telephone(out_df)

    return out_df


def main(args):
    src_file = os.path.join(args.data_root, utils.generate_daily_filename())
    tabular_data = read_stg_json(src_file)

    tabular_data = main_transformation(tabular_data)

    destination = os.path.join(args.data_root, args.final_db)
    write_to_sqlite(destination, tabular_data, args.main_table)


if __name__ == "__main__":
    args = utils.args_from_config("config.ini")
    main(args)
