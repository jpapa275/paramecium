"""
    Utility functions
"""

from pathlib import Path
import pandas as pd
import requests
from colorama import Fore, init


def is_data_frame(data_frame: pd.DataFrame) -> bool:
    """Checks if inputted df is actually a df

    Args:
        data_frame (pd.DataFrame): Takes a df as input

    Raises:
        TypeError: If the 

    Returns:
        bool: 
    """
    if isinstance(data_frame, pd.DataFrame):
        return True
    else:
        raise TypeError(
            f"Input is not a valid Pandas DataFrame.\nType inputted: {type(data_frame)}"
        )


def make_dataframe(data_frame_list: list) -> pd.DataFrame:
    """_summary_

    Args:
        data_frame_list (list): Takes a list

    Raises:
        TypeError: Type error if not list

    Returns:
        pd.DataFrame: Returns the inputted list to a dataframe
    """
    if isinstance(data_frame_list, list):
        data_frame = pd.DataFrame(data_frame_list)
        return data_frame
    else:
        raise TypeError(f"Input is not a list.\nType: {type(data_frame_list)}")

def df_to_db(df):
    if is_data_frame(df) and not df.empty:
        #Need a function to build a sqlalchemy connection
        #Then pass the df to a table in the database
        
        pass

def df_sql_conn():
    #Build a sql connection to a sqlite db file
    pass


def output_csv(data_frame: pd.DataFrame, csv_name):
    """Takes the df and creates a csv

    Args:
        data_frame (pd.DataFrame): Any df
        csv_name (_type_): Name of csv file
    """
    filepath = f"{Path(__file__).resolve().parent}/{csv_name}"
    if filepath.exists() and is_data_frame(data_frame):
        data_frame.to_csv(filepath)


def output_df(data_frame):
    """Outputs the DF with a rounded grid format using tabulate

    Args:
        data_frame (pd.DataFrame): Pandas dataframe to output

    Returns:
        pd.DataFrame: DF with a rounded grid format using tabulate
    """
    if is_data_frame(data_frame):
        return data_frame.to_markdown(tablefmt="rounded_grid", index=False)


def validate_cve(cve_id: str) -> bool:
    """Checks if a cve is valid against the NVD db

    Args:
        cve_id (str): The cve id

    Returns:
        bool: 
    """
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0?cveId="
    url = f"{url}{cve_id.upper()}"
    # make the call to NVD
    try:
        response = requests.get(url=url, timeout=5)
        response.raise_for_status()
        if response.status_code == 200:
            if response.json().get("resultsPerPage") == 1:
                return True
            else:
                return False
    except requests.exceptions as err:
        print_red(err)


def banner():
    init(autoreset=True)
    print(
        Fore.MAGENTA
        + r"""                 _            _ _    
                | |          | | |    
   ___ _____   _| |_ ___   __| | |__  
  / __/ __\ \ / / __/ _ \ / _` | '_ \ 
 | (__\__ \\ V /| || (_) | (_| | |_) |
  \___|___/ \_/  \__\___/ \__,_|_.__/ 
            ______    ______          
           |______|  |______|                                                                        
    """
    )


def print_red(statement):
    init(autoreset=True)
    print(Fore.RED + statement)


def print_green(statement):
    init(autoreset=True)
    print(Fore.GREEN + statement)


def print_yellow(statement):
    init(autoreset=True)
    print(Fore.YELLOW + statement)


def snake_case_df_columns(df: pd.DataFrame):
    """Takes a df and snake cases

    Args:
        df (_type_): _description_

    Returns:
        _type_: Returns the df with columns lowered to snake_case
    """
    if not df.empty and is_data_frame(df):
        df.columns = df.columns.str.lower().str.replace(' ', '_')
        return df.columns
    
    
    # Function to check and correct the database file extension
def check_db_file_extension(db_file):
    """Checks if .db is not file extension provided and adds it

    Args:
        db_file (str): _description_

    Returns:
        str: _description_
    """
    # If the file does not end with '.db'
    if ".db" not in db_file:
        # Create a Path object
        p = Path(db_file)
        # Get the file name without extension
        file_name_without_ext = p.stem
        # Append .db extension and return
        db_file = str(Path(file_name_without_ext).with_suffix(".db"))
    return db_file

# Function to import a CSV file and return a DataFrame
def import_csv(csv_file):
    """_summary_

    Args:
        csv_file (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Read the CSV file into a DataFrame
    csv_df = pd.read_csv(csv_file)
    # Convert column names to snake_case
    csv_df.columns = snake_case_df_columns(csv_df)
    # Print a success message
    print_green(f"[*] Successfully imported the csv file: {csv_file}")
    return csv_df