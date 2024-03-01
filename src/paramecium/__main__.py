
"""Paramecium
"""
import argparse
import pathlib
import sys


from paramecium import (

    csv_to_db,
    kev
)


DEFAULT_DB_PATH = pathlib.Path.home().joinpath("csv_to_db_default.db")


def cli():
    global_parser = argparse.ArgumentParser(
        description="Tools to bump and move to", prog="paramecium"
    )
    subparsers = global_parser.add_subparsers(title="commands")
    csv_parser = subparsers.add_parser(
        "csv_to_db",
        help="Simple CSV (with headers as the columns) to SQLite importer with limited options for limited minds",
    )
    csv_parser.add_argument(
        "-c",
        "--csv_file",
        type=str,
        required=True,
        help="Path and filename to the csv you want to import into a SQLite db",
    )
    csv_parser.add_argument(
        "-d",
        "--db_file",
        type=str,
        required=True,
        default=DEFAULT_DB_PATH,
        help=f"Path to db file. Defaults to current working directory: {DEFAULT_DB_PATH}.",
    )
    csv_parser.add_argument(
        "-t",
        "--table_name",
        type=str,
        required=True,
        help="Name of the table to be created.",
    )
    csv_parser.add_argument(
        "-o",
        "--insert_option",
        type=str,
        default="replace",
        choices=["fail", "replace", "append"],
        help="Three options that will control what happens if the table already exists in the db. Fail, replace or append. Pretty self-explantory.",
    )
    csv_parser.set_defaults(func=csv_to_db.csv_to_db)

    # ip_parser = subparsers.add_parser("ip_info", help="Simple IP Utilities")
    # ip_subparsers = ip_parser.add_subparsers(title="commands")

    # egress_ip_parser = ip_subparsers.add_parser(
    #     "egress_ip", help="Get the current egress IP"
    # )
    # egress_ip_parser.set_defaults(func=ip_info.egress_ip)

    # geolocate_parser = ip_subparsers.add_parser("geolocate", help="Geolocate an IP")
    # geolocate_parser.add_argument(
    #     "-i",
    #     "--ip_address",
    #     type=str,
    #     default=ip_info.get_ip(),
    #     help="IP address to geolocate",
    # )
    # geolocate_parser.set_defaults(func=ip_info.get_ip_location)

    kev_parser = subparsers.add_parser("kev", help="Cisa KEV Utilities")
    kev_subparsers = kev_parser.add_subparsers(title="commands")
    kev_search_parser = kev_subparsers.add_parser(
        "search_kev", help="Search KEV for a single CVE id. Case insensitive"
    )
    kev_search_parser.add_argument(
        "--cve_id",
        type=str,
        help="CVE ID to search for",
    )
    kev_search_parser.set_defaults(func=kev.search_kev_cve)

    args = global_parser.parse_args(args=None if sys.argv[1:] else ["--help"])
    args.func(args)


if __name__ == "__main__":
    cli()
