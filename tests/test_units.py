import json
import os
import pytest
import pandas as pd
from typing import Final

import src.utils as utils
from src.download_json import main as download_json
from src.to_sqlite import read_stg_json, write_to_sqlite


@pytest.fixture
def args():
    return utils.args_from_config("config.ini")


# Tests from the downloading module

def test_download(args):
    download_json(args)
    data_files = os.listdir("data")
    assert "oci.json" in data_files


# Tests from the to_sqlite module

@pytest.fixture
def sample_json() -> dict:
    sample_data = {
        "unused": 1,
        "result": {
            "records": [
                {"addresses_roadtype_name": "",
                 "addresses_end_street_number": None,
                 "values_attribute_name": "",
                 "addresses_road_name": "Pl Arts",
                 "values_category": "",
                 "addresses_zip_code": "8013"}
            ]
        }
    }
    return sample_data


@pytest.fixture
def sample_df() -> pd.DataFrame:
    sample_data = {
        "a": [i for i in range(100)],
        "b": [j*j for j in range(100)]
    }
    return pd.DataFrame(sample_data)


def test_read_json(args, sample_json: dict):
    TEST_FILE_NAME: Final = os.path.join(args.data_root, "test_sample.json")
    with open(TEST_FILE_NAME, "w") as ts:
        json.dump(sample_json, ts)
    df = read_stg_json(TEST_FILE_NAME)
    assert df is not None


def test_to_sqlite(args, sample_df):
    dest_db = os.path.join(args.data_root, args.final_db)
    write_to_sqlite(dest_db, sample_df, "test_table")
    assert True  # just assert that execution completed
