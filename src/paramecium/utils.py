"""
    Utility functions
"""

import pathlib
import pandas as pd
import requests
from colorama import Fore, Style, init


def is_data_frame(data_frame: pd.DataFrame) -> bool:
    if isinstance(data_frame, pd.DataFrame):
        return True
    else:
        raise TypeError(
            f"Input is not a valid Pandas DataFrame.\nType inputted: {type(data_frame)}"
        )


def make_dataframe(data_frame_list: list) -> pd.DataFrame:
    if isinstance(data_frame_list, list):
        data_frame = pd.DataFrame(data_frame_list)
        return data_frame
    else:
        raise TypeError(f"Input is not a list.\nType: {type(data_frame_list)}")


def output_csv(data_frame: pd.DataFrame, csv_name):
    filepath = f"{pathlib.Path(__file__).resolve().parent}/{csv_name}"
    if filepath.exists() and is_data_frame(data_frame):
        data_frame.to_csv(filepath)


def output_df(data_frame):
    """Outputs the DF with a rounded grid format using tabulate

    Args:
        data_frame (pd.DataFrame): Pandas dataframe to output

    Returns:
        pd.DataFrame: _description_
    """
    if is_data_frame(data_frame):
        return data_frame.to_markdown(tablefmt="rounded_grid", index=False)


def validate_cve(cve_id: str) -> bool:
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0?cveId="
    url = f"{url}{cve_id.upper()}"
    # make the call to NVD
    response = requests.get(url=url, timeout=5)
    if response.status_code == 200:
        if response.json().get("resultsPerPage") == 1:
            return True
    return False


def banner():
    init(wrap=False)
    print(
        Fore.RED
        + r"""
 ___      ___ ___  ___  ___       ________   ________  ___       ___     
|\  \    /  /|\  \|\  \|\  \     |\   ___  \|\   ____\|\  \     |\  \    
\ \  \  /  / | \  \\\  \ \  \    \ \  \\ \  \ \  \___|\ \  \    \ \  \   
 \ \  \/  / / \ \  \\\  \ \  \    \ \  \\ \  \ \  \    \ \  \    \ \  \  
  \ \    / /   \ \  \\\  \ \  \____\ \  \\ \  \ \  \____\ \  \____\ \  \ 
   \ \__/ /     \ \_______\ \_______\ \__\\ \__\ \_______\ \_______\ \__\
    \|__|/       \|_______|\|_______|\|__| \|__|\|_______|\|_______|\|__|                                                                           
    """
    )
    print(Style.RESET_ALL)


def print_red(statement):
    init(autoreset=True)
    print(Fore.RED + statement)


def print_green(statement):
    init(autoreset=True)
    print(Fore.GREEN + statement)


def print_yellow(statement):
    init(autoreset=True)
    print(Fore.YELLOW + statement)


def snake_case_pd_columns(df):
    if not df.empty:
        df.columns = df.columns.str.lower().str.replace(' ', '_')
        return df