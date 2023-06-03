import pytest
from types import SimpleNamespace

import src.utils as utils
from src.download_json import query


@pytest.fixture
def args() -> SimpleNamespace:
    return utils.args_from_config("config.ini")


@pytest.fixture
def src_json_data(args) -> dict:
    return query(args)


@pytest.fixture
def data_columns() -> list[str]:
    return ['_id', 'register_id', 'name', 'institution_id', 'institution_name',
            'created', 'modified', 'addresses_roadtype_id', 'addresses_roadtype_name',
            'addresses_road_id', 'addresses_road_name', 'addresses_start_street_number',
            'addresses_end_street_number', 'addresses_neighborhood_id',
            'addresses_neighborhood_name', 'addresses_district_id',
            'addresses_district_name', 'addresses_zip_code', 'addresses_town',
            'addresses_main_address', 'addresses_type', 'values_id',
            'values_attribute_id', 'values_category', 'values_attribute_name',
            'values_value', 'values_outstanding', 'values_description',
            'secondary_filters_id', 'secondary_filters_name',
            'secondary_filters_fullpath', 'secondary_filters_tree',
            'secondary_filters_asia_id', 'geo_epgs_25831_x',
            'geo_epgs_25831_y', 'geo_epgs_4326_x', 'geo_epgs_4326_y']


def test_source_result(src_json_data: dict):
    assert "result" in src_json_data


def test_source_records(src_json_data: dict):
    assert "records" in src_json_data["result"]


def test_source_columns(src_json_data: dict, data_columns: list[str]):
    for column_name in data_columns:
        assert column_name in src_json_data["result"]["records"][0], \
            f"Column {column_name} not in source data"
