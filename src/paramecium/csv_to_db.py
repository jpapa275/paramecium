from sqlalchemy import create_engine, inspect
import pandas as pd
from colorama import Fore, Style
from pathlib import Path


def csv_to_db(args):
    #check if the db_file has .db at the end
    if '.db' not in args.db_file:
        # Create a Path object
        p = Path(args.db_file)

        # Get the file name without extension
        file_name_without_ext = p.stem

        # Append .db extension
        args.db_file = str(Path(file_name_without_ext).with_suffix('.db'))

    # import csv using pandas
    csv_df = pd.read_csv(args.csv_file)
    csv_df.columns = csv_df.columns.str.lower().str.replace(' ', '_')
    print(Fore.GREEN, f"[+] Successfully imported the csv file: {args.csv_file}")

    # build sqlalchemy engine and handle db connection with 'with' statement
    with create_engine(f"sqlite:///{args.db_file}").connect() as connection:
        print(Fore.GREEN, f"[*] Successfully initialized the database: {args.db_file}")

        # take csv dataframe and export to db
        csv_df.to_sql(args.table_name, connection, if_exists=args.insert_option, index=False)

        inspector = inspect(connection)
        if inspector.get_columns(args.table_name):
            df = pd.read_sql(
                f"SELECT count(*) as records_count FROM {args.table_name} LIMIT 1", connection
            )
            if df.empty:
                print(
                    Fore.RED,
                    f"[-] Don't know what you did but it didn't work as nothing was returned from table: {args.table_name}",
                )
            else:
                print(
                    Fore.GREEN,
                    f"[*] Successfully imported {df.iloc[0]['records_count']} records into table: {args.table_name}",
                )
    print(Style.RESET_ALL,end='')
