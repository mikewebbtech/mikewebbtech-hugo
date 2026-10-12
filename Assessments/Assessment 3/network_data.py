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
import os
import subprocess

# Function to clear the console screen, makes it easier to read the output of the programme.
def clear_screen():
    """
    Clear the terminal screen using subprocess.
    (pylint picked up on a deprecated method in the os module, 
    so I used subprocess instead)
    """
    if os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"], check=False)
    else:
        subprocess.run(["clear"], check=False)

# list of network devices
network_devices = [
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
]

# List of IP addresses
network_ip_addresses = [
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
    "10.0.0.1",
    "10.40.2.16"
]

# Dictionary of network services and their corresponding port numbers
network_services_ports = {
    "HTTPS": 443,
    "FTP": 21,
    "SSH": 22,
    "SMTP": 25,
    "DNS": 53,
    "RDP": 3389,
    "LDAP": 389
}

def device_ip():
    """
    Create a dictionary of network devices and their IP addresses.
    The keys are the device names, and the values are the corresponding IP addresses.
    """
    return dict(zip(network_devices, network_ip_addresses))

# Create a usable object of the network devices and IP addresses dictionary
network_devices_dict  = device_ip()

# Display the network devices and their IP addresses
print("Network Devices and their IP Addresses:")
for device, ip in network_devices_dict.items():
    print(f"{device}: {ip}")
