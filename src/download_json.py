import requests
import json


def main():
    base_url = "https://opendata-ajuntament.barcelona.cat/data/api/action/datastore_search"
    parameters = {
        "resource_id": "877ccf66-9106-4ae2-be51-95a9f6469e4c"
    }
    json_filename = "data/oci.json"
    resp = requests.get(base_url, params=parameters)
    with open(json_filename, "w") as jf:
        json.dump(resp.json(), jf)


if __name__ == "__main__":
    main()
