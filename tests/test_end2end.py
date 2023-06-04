import pytest

import src.utils as utils
from src.download_json import main as download_json
from src.to_sqlite import main as to_sqlite


@pytest.fixture
def args():
    return utils.args_from_config("config.ini")


def test_full_pipeline(args):
    try:
        download_json(args)
        to_sqlite(args)
        assert True
    except BaseException as e:
        assert False, f"Pipeline execution failed: {str(e)}"
