"""
Program: Create and manage python lists, dictionaries and TXT file (manage network data)
Requires: Python 3.10 or higher (tested on Python 3.14.3)
Description: Demonstrates Python data structures use:
             - Part A: Manage Python lists and dictionaries of network devices, IP addresses,
                services and ports with ability to search, add, delete and sort by device or
                service name.
             - Part B:  Generate a text report the network devices, IP addresses, network services 
                and port numbers.
Author: Michael Webb
Student ID: 20172813
Date: 2026-11-28
Version: 1.0
"""

# list of network devices
network_devices = {
    "Router",
    "Access Point",
    "Floor 1 Switch",
    "Floor 2 Switch",
    "Firewall",
    "Jump Box",
    "Web Server",
    "Database Server",
    "Development Server",
    "Mail Server",
    "File Server",
    "Active Directory Server"
}

# List of IP addresses
network_ip_addresses = {
    "192.168.1.1",
    "192.168.1.2",
    "192.168.1.3",
    "192.168.1.4", 
    "192.168.2.1",
    "192.168.2.2",
    "192.168.2.3",
    "172.16.0.4",
    "172.16.0.5",
    "172.16.0.6",
    "10.0.0.1"
    "10.40.2.16"
    }

# Dictionary of network devices and their  IP addresses from the network_devices
#  and network_ip_addresses lists.
# The keys are the device names, and the values are the corresponding IP addresses.
network_devices_ip = [
    {"Router": "192.168.1.1"},
    {"Access Point": "192.168.1.2"},
    {"Floor 1 Switch": "192.168.1.3"},
    {"Floor 2 Switch": "192.168.1.4"},
    {"Firewall": "192.168.2.1"},
    {"Jump Box": "192.168.2.2"},
    {"Web Server": "192.168.2.3"},
    {"Database Server": "172.16.0.4"},
    {"Development Server": "172.16.0.5"},
    {"Mail Server": "172.16.0.6"},
    {"File Server": "10.0.0.1"},
    {"Active Directory Server": "10.40.2.16"}
]

# Dictionary of network services and their corresponding port numbers
network_services_ports = [
    {"HTTPS": 443},
    {"FTP": 21},
    {"SSH": 22},
    {"SMTP": 25},
    {"DNS": 53},
    {"RDP": 3389},
    {"LDAP": 389}
]