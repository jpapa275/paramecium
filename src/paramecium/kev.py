""" 
KEV Utilities
"""

import pandas as pd
from paramecium.utils import is_data_frame, output_csv,output_df,validate_cve,print_red,print_green,print_yellow
# import from config.yml
KEV_URL = "https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv"



def get_cisa_kev() -> pd.DataFrame:
    """Get the KEV from a csv and output as dataframe

    Returns:
        pd.Dataframe: KEV DF sorted by date_added
    """
    data_frame = pd.read_csv(KEV_URL)
    if is_data_frame(data_frame):
        data_frame.columns = data_frame.columns.str.replace(
            r"([A-Z]\w+$)", r"_\1", regex=True
        )
        data_frame.columns = data_frame.columns.str.lower()
        return data_frame.sort_values(by="date_added", ascending=False)


def show_kev(data_frame=get_cisa_kev()):
    if is_data_frame(data_frame):
        return output_df(data_frame)


def search_kev_cve(args):
    """Search KEV

    Args:
        search (str): CVE search term like CVE-2023-0000
        data_frame (pd.DataFrame, optional): _description_. Defaults to get_cisa_kev().

    Returns:
        pd.DataFrame: Output of the dataframe to the cli
    """
    if args.cve_id is not None and validate_cve(args.cve_id):
        search = args.cve_id.upper()
        data_frame = get_cisa_kev()
        if is_data_frame(data_frame) and validate_cve(search):
            search_result = data_frame.cve_id.str.contains(
                search, case=False, regex=False
            ).any()
            if search_result:
                print_red("CVE Found in KEV!")
                search_df = data_frame[data_frame.cve_id.values == search]
                return output_df(search_df)
            else:
                print_green("CVE not found in KEV")
    elif not validate_cve(args.cve_id):
        print_yellow(f"Not a valid CVE id according to NIST's NVD. Please check the to make the spelling is correct.\nInput given: {args.cve_id} ")
