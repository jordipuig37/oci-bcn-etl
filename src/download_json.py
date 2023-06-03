import json
import os
import requests

from types import SimpleNamespace

from . import utils


def query(args: SimpleNamespace) -> dict:
    """Queries the API to get Barcelona Oci data in json format."""
    base_url = "https://opendata-ajuntament.barcelona.cat/data/api/action/datastore_search"
    parameters = {
        "resource_id": "877ccf66-9106-4ae2-be51-95a9f6469e4c"
    }
    resp = requests.get(base_url, params=parameters)

    return resp.json()


def main(args: SimpleNamespace):
    data = query(args)
    json_filename = os.path.join(args.data_root, utils.generate_daily_filename())
    os.makedirs(args.data_root, exist_ok=True)
    with open(json_filename, "w") as jf:
        json.dump(data, jf)


if __name__ == "__main__":
    args = utils.args_from_config("config.ini")
    main(args)
