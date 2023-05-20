import datetime as dt
import configparser as cfp

from types import SimpleNamespace


def generate_daily_filename():
    """Return the filename that corresponds the present day with the pattern:
        oci_yyyymmdd.json
    """
    today = dt.datetime.now().strftime("%Y%m%d")
    return f"oci_{today}.json"


def args_from_config(config_file: str) -> SimpleNamespace:
    """Reads a .ini file and return the arguments in DEFAULT section as
    a SimpleNamespace.
    """
    config = cfp.ConfigParser()
    config.read(config_file)
    return SimpleNamespace(**config["DEFAULT"])
