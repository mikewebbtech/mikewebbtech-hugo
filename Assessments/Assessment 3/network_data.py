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

def display_network_devices():
    """
    Iterate through the network devices dictionary and print each device
    and its corresponding IP address.
    """
    clear_screen()
    print("Network Devices and their IP Addresses:")
    for device, ip in network_devices_dict.items():
        print(f"{device} - {ip}")
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
def devices_and_addresses():
    """
    Create a dictionary of network devices and their IP addresses.
    The keys are the device names, and the values are the corresponding IP addresses.
    """
    return dict(zip(network_devices, network_ip_addresses))


# Create a usable object of the network devices and IP addresses dictionary
network_devices_dict = devices_and_addresses()
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

    # Update the dictionary with the new_device key and new_ip value
    network_devices_dict[new_device] = new_ip

    print(f"Added {new_device} with IP address {new_ip} to the network devices lists.")
#-------------------------------------------------------------------------------------------------

# 6. Create a function which ask the user to enter the name of an existing network device to delete.
# Remove the device and its corresponding IP address from the list and dictionary.
# Required test: Delete:  Printer01 – 192.168.1.20
#-------------------------------------------------------------------------------------------------

# 7. Create a function which allows the user to choose what data to sort:
#   Network devices: Sort alphabetically by device name.
#   Network services: Sort alphabetically by service name.
# Display the sorted results.
def sort_network_devices():
    """
    Sort the network devices dictionary by device name and display the sorted list.
    """
    clear_screen()
    sorted_devices = dict(sorted(network_devices_dict.items()))
    print("Sorted Network Devices and their IP Addresses:")
    for device, ip in sorted_devices.items():
        print(f"{device}: {ip}")

def sort_network_services():
    """
    Sort the network services dictionary by service name and display the sorted list.
    """
    clear_screen()
    sorted_services = dict(sorted(network_services_ports.items()))
    print("Sorted Network Services and their Port Numbers:")
    for service, port in sorted_services.items():
        print(f"{service}: {port}")
#-------------------------------------------------------------------------------------------------

# 8. Create a function which allows the user to choose what data to search:
#   Network devices: Search by device name and display its IP address.
#   Network services: Search by service name and display its port number.
def search_network_device():
    """
    Search for a network device by name and display its IP address.
    """
    clear_screen()
    search_term = input("Enter the name of the network device to search for: ")
    found = False
    for device, ip in network_devices_dict.items():
        if search_term.lower() in device.lower():
            print(f"Found -> {device}: {ip}")
            found = True
    if not found:
        print("No matching network devices found.")
    input("\nPress Enter to return to the main menu")

def search_network_service():
    """
    Search for a network service by name and display its port number.
    """
    clear_screen()
    search_term = input("Enter the name of the network service to search for: ")
    found = False
    for service, port in network_services_ports.items():
        if search_term.lower() in service.lower():
            print(f"Found -> {service}: {port}")
            found = True
    if not found:
        print("No matching network services found.")
    input("\nPress Enter to return to the main menu")

def search_dict():
    """Search for a key in the selected dictionary."""
    print("Select dictionary to search:")
    print("1. Network Devices")
    print("2. Network Services")
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        search_network_device()
    elif choice == '2':
        search_network_service()
    clear_screen()
    selected_dict, selected_name = network_devices_dict
    if selected_dict is not None:
        print("--------------------------------------------------")
        print(f"Searching {selected_name}")
        print("--------------------------------------------------")
        search_term = input("Enter key/name to search for: ")
        found = False
        for key, value in selected_dict.items():
            if search_term.lower() in key.lower():
                print(f"Found -> {key}: {value}")
                found = True
        if not found:
            print("No matching items found.")
        print("--------------------------------------------------")
        input("\nPress Enter to return to the main menu")
    else:
        print("Returning to Main Menu")
#-------------------------------------------------------------------------------------------------

def main_menu():
    """Display the main menu."""
    print("\n****  Menu  ****\n")
    print("1. Access Network Devices and IP Addresses")
    print("2. Search Network Devices or Services")
    print("3. Delete a Network Device")
    print("4. Sort Network Devices or Services")
    print("5. Display Network Devices and IP Addresses")
    print("6. Display Network Services and Port Numbers")
    print("\n7. Exit Programme")
    print("****************\n")
