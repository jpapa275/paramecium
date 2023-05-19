import pandas as pd
from sqlalchemy import create_engine, inspect
from colorama import Fore


def csv_to_db(args):
    # import csv using pandas
    csv_df = pd.read_csv(args.csv_file)
    print(Fore.GREEN, f"Successfully imported the csv file: {args.csv_file}")
    # build sqlalchemy engine
    engine = create_engine(f"sqlite:///{args.db_file}")
    print(Fore.GREEN, f"Successfully initialized the database: {args.db_file}")
    # take csv dataframe and export to db
    csv_df.to_sql(args.table_name, engine, if_exists=args.input_option, index=False)

    inspector = inspect(engine)
    if inspector.get_columns(args.table_name):
        df = pd.read_sql(
            f"SELECT count(*) as records_count FROM {args.table_name} LIMIT 1", engine
        )
        if df.empty:
            print(
                Fore.RED,
                f"Don't know what you did but it didn't work as nothing was returned from table: {args.table_name}",
            )
        else:
            print(
                Fore.GREEN,
                f"Successfully imported {df.iloc[0]['records_count']} records into table: {args.table_name}",
            )
