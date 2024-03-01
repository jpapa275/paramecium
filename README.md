# paramecium
A collection of little utilities that I sometimes use

Install by running `pip install .` from this directory.

## Halp
How to use? Read the help by running `paramecium -h`
![image](/imgs/paramecium_help.png "help me")

## Commands

### csv_to_db
A simple csv to db importer. Help: `paramecium csv_to_db -h`

![image](/imgs/csv_to_db_help.png "help me")

### ip_info
- egress_ip
    - Returns the current egress ip of the machine it is being run from.

- geolocate

    ![image](/imgs/ip_info_geolocate_help.png "help me")

    - `-i` argument takes a single IP Address and returns the following info
        
        ![image](/imgs/ge.png "help me")

### kev

CISA KEV Search by cve id

![image](/imgs/kev.png "help me")

- search_kev

    ![image](/imgs/kev_search.png "help me")

    - `--cve_id` argument takes a CVE ID like CVE-2023-1010 and returns details if the CVE ID is in the KEV