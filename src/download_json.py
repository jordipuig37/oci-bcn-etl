import json
import os
import requests

from types import SimpleNamespace

from . import utils

def main(args: SimpleNamespace):
    base_url = "https://opendata-ajuntament.barcelona.cat/data/api/action/datastore_search"
    parameters = {
        "resource_id": "877ccf66-9106-4ae2-be51-95a9f6469e4c"
    }
    os.makedirs(args.data_root, exist_ok=True)
    json_filename = os.path.join(args.data_root, utils.generate_daily_filename())
    resp = requests.get(base_url, params=parameters)
    with open(json_filename, "w") as jf:
        json.dump(resp.json(), jf)


if __name__ == "__main__":
    args = utils.args_from_config("config.ini")
    main(args)
