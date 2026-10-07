import string
import secrets


class PasswordGenerator:

    def generate_password(self, length):
        characters = (
            string.ascii_letters
            + string.digits
            + string.punctuation
        )

        password = ""

        for _ in range(length):
            password += secrets.choice(characters)

        return password

    def save_password(self, password):
        with open("passwords.txt", "a") as file:
            file.write(password + "\n")

        print("\nPassword saved successfully!")