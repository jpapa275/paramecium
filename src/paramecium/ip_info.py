import requests
from tabulate import tabulate


def get_ip():
    response = requests.get("https://api64.ipify.org?format=json", timeout=5).json()
    ip = response.get("ip")
    return ip


def egress_ip(args, ip_address=get_ip()):
    data = [["egress_ip", ip_address]]
    # Print the table
    print(tabulate(data, tablefmt="fancy_grid"))


def get_ip_location(args):
    response = requests.get(
        f"https://ipapi.co/{args.ip_address}/json/", timeout=5
    ).json()
    location_data = {
        "ip": response.get("ip"),
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "asn": response.get("asn"),
        "aso": response.get("org"),
    }

    # Create a table
    table = [["Key", "Value"]]
    for key, value in location_data.items():
        table.append([key, value])

    # Print the table
    print(tabulate(table, tablefmt="fancy_grid"))
