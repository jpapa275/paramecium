""" csv_to_db
"""
from sqlalchemy import create_engine, inspect, text
from paramecium.utils import (
    banner,
    print_green,
    print_red,
    check_db_file_extension,
    import_csv
)





# Function to inspect a table in the database
def inspect_table(db_file, table_name):
    """_summary_

    Args:
        db_file (_type_): _description_
        table_name (_type_): _description_
    """
    # Create a connection to the database
    engine = create_engine(f"sqlite:///{db_file}")
    with engine.connect() as connection:
        try:
            # Create an inspector and check if the table exists
            inspector = inspect(connection)
            if inspector.has_table(table_name):
                # If the table exists, count the number of records
                query = text(f"SELECT COUNT(*) as count FROM {table_name}")
                result = connection.execute(query)
                count = result.scalar()
                # Print a success message
                print_green(f"[*] Successfully imported {count} records into table: {table_name}")
            else:
                # If the table does not exist, print an error message
                print_red(f"[-] The table: {table_name} does not exist")
        except Exception as e:
            # If an error occurs, print an error message
            print_red(f"[-] An error occurred: {e}")

# Function to connect to the database and export a DataFrame to a table
def connect_to_db_and_export_to_table(db_file, table_name, csv_df, insert_option):
    """_summary_

    Args:
        db_file (_type_): _description_
        table_name (_type_): _description_
        csv_df (_type_): _description_
        insert_option (_type_): _description_
    """
    # Create a connection to the database
    engine = create_engine(f"sqlite:///{db_file}")
    with engine.connect() as connection:
        try:
            # Print a success message
            print_green(f"[*] Successfully connected to the database: {db_file}")
            # Export the DataFrame to the table
            csv_df.to_sql(table_name, connection, if_exists=insert_option, index=False)
        except  Exception as err:
            # If an error occurs, print an error message
            print_red(f"[-] An error occurred: {err}")

# Main function to import a CSV file and export it to a database table
def csv_to_db(args):
    """_summary_

    Args:
        args (_type_): _description_

    Raises:
        err: _description_
        err: _description_
    """
    try:
        # Print the banner
        banner()
        # Check and correct the database file extension
        args.db_file = check_db_file_extension(args.db_file)
        # Import the CSV file as a df
        csv_df = import_csv(args.csv_file)
    except Exception as err:
        raise err
    try:
        # Connect to the database and export the DataFrame to the table
        connect_to_db_and_export_to_table(
            args.db_file, args.table_name, csv_df, args.insert_option
        )
        # Inspect the table
        inspect_table(args.db_file, args.table_name)
    except Exception as err:
        raise err
