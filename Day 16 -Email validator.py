import re


def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    return re.match(pattern, email) is not None


def check_email():
    email = input("\nEnter email address: ").strip()

    if not email:
        print("❌ Email cannot be empty.")
        return

    if validate_email(email):
        print("✅ Valid email address!")

        username, domain = email.split("@")

        print(f"👤 Username : {username}")
        print(f"🌐 Domain   : {domain}")

    else:
        print("❌ Invalid email address.")
        print("💡 Example: user@example.com")


def main():

    print("=" * 45)
    print("          📧 EMAIL VALIDATOR")
    print("=" * 45)

    while True:

        print("""
1. 📧 Check Email
2. 🚪 Exit
""")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            check_email()

        elif choice == "2":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice.")


main()