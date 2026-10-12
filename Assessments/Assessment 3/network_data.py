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
# Import necessary modules
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
#-------------------------------------------------------------------------------------------------

# 1.	Create a list that stores at least 12 network device names.
network_devices = [
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
    "Router",
    "Active Directory Server"
]
#-------------------------------------------------------------------------------------------------

# 2. Create a list that stores at least 12 IP address.
# The position of each IP address must correspond to the network device in the first list.
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
#-------------------------------------------------------------------------------------------------

# 3. Create a dictionary using the network device names (step 1) as keys
# and the corresponding IP addresses (step 2) as values.
# The dictionary must be created using the two lists from Steps 1 and 2.
def devices_and_ips():
    """
    Create a dictionary of network devices and their IP addresses.
    The keys are the device names, and the values are the corresponding IP addresses.
    """
    return dict(zip(network_devices, network_ip_addresses))
#-------------------------------------------------------------------------------------------------

# 4. Create a dictionary that stores at least 5 common network services
# and their associated port numbers.
network_services_ports = {
    "HTTPS": 443,
    "FTP": 21,
    "SSH": 22,
    "SMTP": 25,
    "DNS": 53,
    "RDP": 3389,
    "LDAP": 389
}
#-------------------------------------------------------------------------------------------------

# 5. Create a function which ask the user to enter a new device name and IP address,
# then add them to the network device list and dictionary.
# Required test: Provide screenshot for below test:
# Wireless Controller - 192.168.1.5
def add_network_device():
    """
    Ask the user to enter a new device name and IP address,
    then add them to the network device list and dictionary.
    """
    clear_screen()
    new_device = input("Enter the name of the new network device: ")
    new_ip = input("Enter the IP address of the new network device: ")

    # Add to the network device list
    network_devices.append(new_device)
    # Add to the network IP address list
    network_ip_addresses.append(new_ip)

    # Update the dictionary
    network_devices_dict[new_device] = new_ip

    print(f"Added {new_device} with IP address {new_ip} to the network devices.")
#-------------------------------------------------------------------------------------------------


# 6.	Create a function which ask the user to enter the name of an existing network device to delete.
# Remove the device and its corresponding IP address from the list and dictionary.
# Required test: Delete:
# Printer01 – 192.168.1.20

# 7. Create a function which allows the user to choose what data to sort:
#   Network devices: Sort alphabetically by device name.
#   Network services: Sort alphabetically by service name.
# Display the sorted results.

# 8. Create a function which allows the user to choose what data to search:
#   Network devices: Search by device name and display its IP address.
#   Network services: Search by service name and display its port number.


# Create a usable object of the network devices and IP addresses dictionary
network_devices_dict  = devices_and_ips()

# Display the network devices and their IP addresses
def display_network_devices():
    """
    Display the network devices and their corresponding IP addresses.
    """
    clear_screen()
    print("Network Devices and their IP Addresses:")
    for device, ip in network_devices_dict.items():
        print(f"{device} - {ip}")


def sort_network_devices():
    """
    Sort the network devices dictionary by device name and display the sorted list.
    """
    clear_screen()
    sorted_devices = dict(sorted(network_devices_dict.items()))
    print("Sorted Network Devices and their IP Addresses:")
    for device, ip in sorted_devices.items():
        print(f"{device}: {ip}")


display_network_devices()

sort_network_devices()
