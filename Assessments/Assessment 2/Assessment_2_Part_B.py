"""
Part B
In the second part of this assessment, you must design, code, and test a Python program that 
uses a dictionary data structure.

Use the following scenario:
7.	A dictionary that stores at least 12 of your favourite actors/actresses’ names and birthdays.
8.	A dictionary that stores at least 12 of your favourite movies and release year.
9.	A dictionary that stores at least 12 of your favourite games and release year.
10.	Write a Python program that provides the ability to:
10.1.	Create a dictionary from the scenario above
10.2.	Add a value to the dictionary
10.3.	Delete a value from the dictionary
10.4.	Sort all the data in the dictionary in the ascending order. Sort all the data in the 
        dictionary in the descending order.
10.5.	Search for the value in the dictionary asking user for input.
11.	Debug and test your program. You must conduct program tests to test the functionality 
    specified above
"""
import os

# Date format chosen for readability vs ISO8601 formate (YYYY-MM-DD).
# Since sorting will be done on keys, this is fine.
actor_birthday = {
    "Tom Hardy": "15 September 1977",
    "Jake Gyllenhaal": "19 December 1980",
    "Denzel Washington": "28 December 1954",
    "Scarlett Johansson": "22 November 1984",
    "Leonardo DiCaprio": "11 November 1974",
    "Nicole Kidman": "20 June 1967",
    "Morgan Freeman": "1 June 1937",
    "Cate Blanchett": "14 May 1969",
    "Brad Pitt": "18 December 1963",
    "Helen Mirren": "26 July 1945",
    "Keanu Reeves": "2 September 1964",
    "Emma Stone": "6 November 1988"
}

movie_year = {
    "Star Wars": "1977",
    "Resident Evil": "2002",
    "The Dark Knight": "2008",
    "Pulp Fiction": "1994",
    "Forrest Gump": "1994",
    "Interstellar": "2014",
    "Gladiator": "2000",
    "The Matrix": "1999",
    "Superman": "1978",
    "Jurassic Park": "1993",
    "Avatar": "2009",
    "The Avengers": "2012"
}

game_year = {
    "Defender": "1981",
    "Sid Meier’s Civilization": "1991",
    "Tetris": "1984",
    "The Legend Of Zelda": "1986",
    "SimCity": "1989",
    "Diablo": "1996",
    "Super Mario": "1985",
    "Halo": "2001",
    "Doom": "1993",
    "Quake": "1996",
    "Gears of War": "2006",
    "Team Fortress": "1996"
}

def main_menu():
    """Display the main menu."""
    print("\n****  Menu  ****\n")
    print("1. Display List")
    print("2. Add a Favorite")
    print("3. Delete a Favorite")
    print("4. Sort List (Ascending)")
    print("5. Sort List (Descending)")
    print("6. Search Favorites")
    print("\n7. Exit Programme")
    print("****************\n")

def clear_screen():
    """Clear the console screen based on the operating system."""
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def dict_menu():
    """Display the dictionary menu and return the selected dictionary and its name."""
    while True:
        clear_screen()
        print("\n****  Available Dictionaries  ****\n")
        print("1. Actors and Birthdays")
        print("2. Movies  andRelease Year")
        print("3. Games and Release Years")
        print("4. Return to main Menu")
        print("**********************************\n")

        dict_choice = input("Enter your dictionary choice (1-4): ")

        if dict_choice == '1':
            return actor_birthday, "Actors and Birthdays"
        if dict_choice == '2':
            return movie_year, "Movies and Release Years"
        if dict_choice == '3':
            return game_year, "Games and Release Years"
        if dict_choice == '4':
            print("Returning to Main Menu")
            return None, None
        print("Invalid choice. Please enter a number between 1 and 4.")
        input("Press Enter to continue.")

def view_dict():
    """Display the selected dictionary."""
    clear_screen()
    selected_dict, selected_name = dict_menu()
    if selected_dict is not None:
        print("--------------------------------------------------")
        print(f"Displaying {selected_name}")
        print("--------------------------------------------------")
        for key, value in selected_dict.items():
            print(f"{key}: {value}")
        print("--------------------------------------------------")
        input("\nPress Enter to return to the main menu")
    else:
        print("Returning to Main Menu")

def sort_dict():
    """Display the selected dictionary in ascending key order."""
    clear_screen()
    selected_dict, selected_name = dict_menu()
    if selected_dict is not None:
        print("--------------------------------------------------")
        print(f"Sorting {selected_name} (Ascending by Key)")
        print("--------------------------------------------------")
        # Sort dictionary keys alphabetically
        sorted_keys = sorted(selected_dict.keys())
        for key in sorted_keys:
            print(f"{key}: {selected_dict[key]}")
        print("--------------------------------------------------")
        input("\nPress Enter to return to the main menu")
    else:
        print("Returning to Main Menu")

def sort_dict_desc():
    """Display the selected dictionary in descending key order."""
    clear_screen()
    selected_dict, selected_name = dict_menu()
    if selected_dict is not None:
        print("--------------------------------------------------")
        print(f"Sorting {selected_name} (Descending by Key)")
        print("--------------------------------------------------")
        # Sort dictionary keys in reverse alphabetical order
        sorted_keys = sorted(selected_dict.keys(), reverse=True)
        for key in sorted_keys:
            print(f"{key}: {selected_dict[key]}")
        print("--------------------------------------------------")
        input("\nPress Enter to return to the main menu")
    else:
        print("Returning to Main Menu")

def search_dict():
    """Search for a key in the selected dictionary."""
    clear_screen()
    selected_dict, selected_name = dict_menu()
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

def add_dict():
    """Add a key-value pair to the selected dictionary."""
    clear_screen()
    selected_dict, selected_name = dict_menu()
    if selected_dict is not None:
        print("--------------------------------------------------")
        print(f"Adding entry to {selected_name}")
        print("--------------------------------------------------")
        key = input("Enter name (Key): ")
        value = input("Enter birthday or release year (Value): ")
        selected_dict[key] = value
        print(f"'{key}: {value}' added successfully.")
        print("--------------------------------------------------")
        input("\nPress Enter to return to the main menu")
    else:
        print("Returning to Main Menu")

def delete_dict():
    """Delete a key-value pair from the selected dictionary."""
    clear_screen()
    selected_dict, selected_name = dict_menu()
    if selected_dict is not None:
        print("--------------------------------------------------")
        print(f"Deleting entry from {selected_name}")
        print("--------------------------------------------------")
        key = input("Enter the name/key to delete: ")
        if key in selected_dict:
            del selected_dict[key]
            print(f"'{key}' deleted successfully.")
        else:
            print(f"'{key}' not found in dictionary.")
        print("--------------------------------------------------")
        input("\nPress Enter to return to the main menu")
    else:
        print("Returning to Main Menu")

# Menu Selection Loop
while True:
    clear_screen()
    main_menu()
    choice = input("Enter your choice (1-7): ")
    if choice == '1':
        print("Select list to display: ")
        view_dict()
    elif choice == '2':
        add_dict()
    elif choice == '3':
        delete_dict()
    elif choice == '4':
        sort_dict()
    elif choice == '5':
        sort_dict_desc()
    elif choice == '6':
        search_dict()
    elif choice == '7':
        print("exiting program. goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
        input("Press Enter to continue.")
        continue

#- END OF PROGRAMME ---------------------------------------------------------------
