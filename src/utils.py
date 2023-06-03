import configparser as cfp
import datetime as dt
import functools as ft
import pandas as pd

from types import SimpleNamespace
from typing import Callable


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


def use_copy(
        func: Callable[[pd.DataFrame], pd.DataFrame]
        ) -> Callable[[pd.DataFrame], pd.DataFrame]:
    """Decorates a function that takes a single dataframe as input, to make a
    copy of the input dataframe and avoid accidentally make changes to the
    original one.
    """
    @ft.wraps(func)
    def wrapper(df: pd.DataFrame) -> pd.DataFrame:
        df_copy = df.copy()
        return func(df_copy)
    return wrapper
