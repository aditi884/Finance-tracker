import json
import os
import re

# Define the file name for data persistence
DATA_FILE = "contacts.json"

class ContactBook:
    """
    A console-based Contact Book Manager.
    Allows adding, viewing, searching, and deleting contacts.
    """
    def __init__(self):
        """
        Initializes the ContactBook by loading contacts from a file.
        """
        self.contacts = {}
        self.load_data()

    def _save_data(self):
        """
        Saves the current contacts dictionary to a JSON file.
        """
        try:
            with open(DATA_FILE, 'w') as f:
                json.dump(self.contacts, f, indent=4)
            print(f"\nContacts saved successfully to {DATA_FILE}")
        except IOError:
            print(f"\nError: Could not save contacts to {DATA_FILE}")

    def load_data(self):
        """
        Loads contact data from a JSON file.
        """
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r') as f:
                    self.contacts = json.load(f)
                print(f"\nContacts loaded successfully from {DATA_FILE}")
            except (IOError, json.JSONDecodeError):
                print(f"\nError: Could not load data from {DATA_FILE}. Starting with an empty contact book.")
                self.contacts = {}
        else:
            print(f"\nNo data file found ({DATA_FILE}). Starting with a new, empty contact book.")

    def add_contact(self):
        """
        Prompts the user for a new contact's details and adds it to the book.
        """
        print("\n--- Add a New Contact ---")
        name = input("Enter contact's name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return

        # Check for existing contact with the same name
        if name in self.contacts:
            print(f"Error: A contact named '{name}' already exists.")
            return

        phone = input("Enter phone number: ").strip()
        email = input("Enter email address: ").strip()
        
        # Simple email validation
        if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email format.")
            return
            
        self.contacts[name] = {
            "phone": phone,
            "email": email
        }
        print(f"Contact '{name}' added successfully!")
        self._save_data()

    def view_all_contacts(self):
        """
        Displays all contacts in the book, sorted alphabetically by name.
        """
        if not self.contacts:
            print("\nNo contacts found.")
            return

        print("\n--- All Contacts ---")
        # Sort contacts by name for a clean display
        sorted_names = sorted(self.contacts.keys())

        for name in sorted_names:
            contact = self.contacts[name]
            print(f"Name: {name}")
            print(f"  Phone: {contact['phone']}")
            print(f"  Email: {contact['email']}")
            print("-" * 20)

    def search_contact(self):
        """
        Searches for a contact by name and displays their details.
        """
        print("\n--- Search for a Contact ---")
        name_to_search = input("Enter the name of the contact to search for: ").strip()
        
        if name_to_search in self.contacts:
            contact = self.contacts[name_to_search]
            print(f"\nContact Found:")
            print(f"  Name: {name_to_search}")
            print(f"  Phone: {contact['phone']}")
            print(f"  Email: {contact['email']}")
        else:
            print(f"Contact '{name_to_search}' not found.")

    def delete_contact(self):
        """
        Deletes a contact from the book by name.
        """
        print("\n--- Delete a Contact ---")
        name_to_delete = input("Enter the name of the contact to delete: ").strip()
        
        if name_to_delete in self.contacts:
            del self.contacts[name_to_delete]
            print(f"Contact '{name_to_delete}' deleted successfully.")
            self._save_data()
        else:
            print(f"Contact '{name_to_delete}' not found.")

    def run(self):
        """
        Main loop to run the application.
        """
        while True:
            print("\n--- Main Menu ---")
            print("1. Add a new contact")
            print("2. View all contacts")
            print("3. Search for a contact")
            print("4. Delete a contact")
            print("5. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_all_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.delete_contact()
            elif choice =
