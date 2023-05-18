"""
csv_to_db
"""
import pathlib

import click
import pandas as pd
from sqlalchemy import create_engine, inspect

DEFAULT_DB_PATH = pathlib.Path.cwd().joinpath("csv_to_db_default.db")


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "-c",
    "--csv_file",
    type=click.Path(
        exists=True,
    ),
    required=True,
    help="path and filename to the csv you want to import",
)


@click.option(
    "-d",
    "--db_file",
    required=True,
    default=DEFAULT_DB_PATH,
    help=f"Path to db file. Defaults to current working directory: {DEFAULT_DB_PATH}",
)


@click.option(
    "-t",
    "--table_name",
    required=True,
    type=str,
    help="Name of the table you want created",
)


@click.option(
    "-o",
    "--table_option",
    default="replace",
    type=click.Choice(["fail", "replace", "append"]),
    help="Three options that will control what happens if the table already exists in the db. Fail, replace or append. Pretty self-explantory.",
)


def main(csv_file, db_file, table_name, table_option):
    """
    Simple CSV (with headers) to SQLite importer with limited options for limited minds
    """
    # import csv using pandas
    csv_df = pd.read_csv(csv_file)
    click.echo(f"Successfully imported the csv file: {csv_file}")
    # build sqlalchemy engine
    engine = create_engine(f"sqlite:///{db_file}")
    click.echo("Successfully initialized the database")
    # take csv dataframe and export to db
    csv_df.to_sql(table_name, engine, if_exists=table_option, index=False)

    inspector = inspect(engine)
    if inspector.get_columns(table_name):
        df = pd.read_sql(
            f"SELECT count(*) as records_count FROM {table_name} LIMIT 1", engine
        )
        if df.empty:
            click.secho(
                f"Don't know what you did but it didn't work as nothing was returned from table: {table_name}",
                err=True,
                fg="red",
            )
        else:
            click.secho(
                f"Successfully inserted {df['records_count'].to_string(index=False)} records from the csv into database table: {table_name}",
                fg="green",
            )
            # click.echo(df.to_markdown(tablefmt="rounded_grid",index=False))
