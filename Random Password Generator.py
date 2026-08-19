import random
import string


def generate_password(length):

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


print("=" * 50)
print("        🔐 RANDOM PASSWORD GENERATOR")
print("=" * 50)

while True:

    try:
        length = int(
            input("\nEnter password length (minimum 6): ")
        )

        if length < 6:
            print("❌ Password length must be at least 6.")
            continue

        password = generate_password(length)

        print("\n🎉 Generated Password:")
        print(password)

        again = input(
            "\nGenerate another password? (y/n): "
        ).lower()

        if again != "y":
            print("\n👋 Password Generator closed.")
            break

    except ValueError:
        print("❌ Please enter a valid number.")