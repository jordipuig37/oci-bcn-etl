import pytest
import pandas as pd

from src.to_sqlite import standarize_telephone, transform_telephone, transform_filter_nulls


@pytest.fixture
def input_data():
    # Create the source DataFrame for testing
    source_data = {
        "register_id": [1, 2, 3, 4, None, 6],
        "name": ["John", "Jane", "Mike", "Alice", "Johan", None],
        "Age": [25, None, 30, None, 23, 24],
        "City": ["New York", "London", None, None, "Seattle", "Austin"],
        "Telephone": ["(123) 456-7890", "987-654-3210", "abcHelloWorld -!,.",
                      "(555) 123-4567", "93 322 98 21 21", "not a telephone"]
    }
    return pd.DataFrame(source_data)


@pytest.fixture
def target_data_filter_null():
    # Create the target DataFrame for testing transform_filter_nulls
    target_data = {
        "register_id": [1.0, 2, 3, 4],
        "name": ["John", "Jane", "Mike", "Alice"],
        "Age": [25, None, 30, None],
        "City": ["New York", "London", None, None],
        "Telephone": ["(123) 456-7890", "987-654-3210", "abcHelloWorld -!,.", "(555) 123-4567"]
    }
    return pd.DataFrame(target_data)


@pytest.fixture
def target_data_telephone():
    # Create the target DataFrame for testing transform_telephone
    target_data = {
        "register_id": [1, 2, 3, 4, None, 6],
        "name": ["John", "Jane", "Mike", "Alice", "Johan", None],
        "Age": [25, None, 30, None, 23, 24],
        "City": ["New York", "London", None, None, "Seattle", "Austin"],
        "Telephone": [1234567890, 9876543210, -1, 5551234567, 93322982121, -1]
    }
    return pd.DataFrame(target_data)


def test_standarize_telephone_valid_input():
    tel = "(123) 456-7890"
    result = standarize_telephone(tel)
    assert result == 1234567890


def test_standarize_telephone_invalid_input():
    tel = "abcHelloWorld -!,."
    result = standarize_telephone(tel)
    assert result == -1


def test_transform_telephone(input_data, target_data_telephone):
    # Call the transform_telephone function
    transformed_df = transform_telephone(input_data)

    pd.testing.assert_frame_equal(transformed_df, target_data_telephone)


def test_transform_filter_nulls(input_data, target_data_filter_null):
    # Call the transform_filter_nulls function
    transformed_df = transform_filter_nulls(input_data)

    pd.testing.assert_frame_equal(transformed_df, target_data_filter_null)
