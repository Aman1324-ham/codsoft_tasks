from contact_manager.contacts import ContactBook


def display_menu():
    print("\n==========================")
    print("      CONTACT BOOK")
    print("==========================")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("==========================")


def main():
    contact_book = ContactBook()

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n--- Add Contact ---")

            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")

            if not name:
                print("\nName cannot be empty.")
                continue

            contact_book.add_contact(name, phone, email)

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            keyword = input("\nEnter name, phone or email to search: ")

            if keyword:
                contact_book.search_contact(keyword)
            else:
                print("\nSearch cannot be empty.")

        elif choice == "4":
            name = input("\nEnter the name of the contact to update: ")

            if name:
                contact_book.update_contact(name)
            else:
                print("\nName cannot be empty.")

        elif choice == "5":
            name = input("\nEnter the name of the contact to delete: ")

            if name:
                contact_book.delete_contact(name)
            else:
                print("\nName cannot be empty.")

        elif choice == "6":
            print("\nThank you for using Contact Book!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()