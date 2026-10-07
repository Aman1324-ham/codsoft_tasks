from generator.password import PasswordGenerator


def display_menu():
    print("\n==============================")
    print("       PASSWORD GENERATOR")
    print("==============================")
    print("1. Generate Password")
    print("2. Generate and Save Password")
    print("3. Exit")
    print("==============================")


def get_length():
    while True:
        try:
            length = int(input("Enter password length: "))

            if length < 4:
                print("Password length should be at least 4.")
            else:
                return length

        except ValueError:
            print("Please enter a valid number.")


def main():

    generator = PasswordGenerator()

    while True:

        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":

            length = get_length()

            password = generator.generate_password(length)

            print("\nGenerated Password:")
            print(password)

        elif choice == "2":

            length = get_length()

            password = generator.generate_password(length)

            print("\nGenerated Password:")
            print(password)

            generator.save_password(password)

        elif choice == "3":

            print("\nThank you for using Password Generator!")
            break

        else:

            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()