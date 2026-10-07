import json
import os


class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = []
        self.load_contacts()

    # Load contacts from JSON file
    def load_contacts(self):
        if not os.path.exists(self.filename):
            self.contacts = []
            self.save_contacts()
            return

        try:
            with open(self.filename, "r") as file:
                self.contacts = json.load(file)

        except (json.JSONDecodeError, FileNotFoundError):
            self.contacts = []

    # Save contacts to JSON file
    def save_contacts(self):
        with open(self.filename, "w") as file:
            json.dump(self.contacts, file, indent=4)

    # Add a new contact
    def add_contact(self, name, phone, email):
        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        self.contacts.append(contact)
        self.save_contacts()

        print("\nContact added successfully!")

    # Display all contacts
    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts found.")
            return

        print("\n----- Contact List -----")

        for number, contact in enumerate(self.contacts, start=1):
            print(f"\nContact {number}")
            print(f"Name  : {contact['name']}")
            print(f"Phone : {contact['phone']}")
            print(f"Email : {contact['email']}")

    # Search contact
    def search_contact(self, keyword):
        found = False

        for contact in self.contacts:
            if (keyword.lower() in contact["name"].lower()
                    or keyword in contact["phone"]
                    or keyword.lower() in contact["email"].lower()):

                print("\nContact found:")
                print(f"Name  : {contact['name']}")
                print(f"Phone : {contact['phone']}")
                print(f"Email : {contact['email']}")

                found = True

        if not found:
            print("\nNo matching contact found.")

    # Delete contact
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact["name"].lower() == name.lower():
                self.contacts.remove(contact)
                self.save_contacts()

                print("\nContact deleted successfully!")
                return

        print("\nContact not found.")

    # Update contact
    def update_contact(self, name):
        for contact in self.contacts:
            if contact["name"].lower() == name.lower():

                print("\nLeave a field empty if you don't want to change it.")

                new_name = input(f"New name [{contact['name']}]: ")
                new_phone = input(f"New phone [{contact['phone']}]: ")
                new_email = input(f"New email [{contact['email']}]: ")

                if new_name:
                    contact["name"] = new_name

                if new_phone:
                    contact["phone"] = new_phone

                if new_email:
                    contact["email"] = new_email

                self.save_contacts()

                print("\nContact updated successfully!")
                return

        print("\nContact not found.")