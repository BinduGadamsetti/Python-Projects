contacts = {}


def add_contact():
    print("\n--- ➕ Add Contact ---")

    name = input("Enter name: ").strip().title()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip().lower()

    if not name or not phone:
        print("❌ Name and phone number are required.")
        return

    if phone in contacts:
        print("❌ A contact with this phone number already exists.")
        return

    contacts[phone] = {
        "name": name,
        "email": email
    }

    print("✅ Contact added successfully!")


def view_contacts():
    print("\n--- 📒 All Contacts ---")

    if not contacts:
        print("📭 No contacts found.")
        return

    for number, contact in contacts.items():
        print(f"\n👤 {contact['name']}")
        print(f"📞 {number}")
        print(f"📧 {contact['email'] or 'Not provided'}")


def search_contact():
    keyword = input("\n🔍 Enter name to search: ").strip().lower()

    found = False

    for number, contact in contacts.items():

        if keyword in contact["name"].lower():
            print("\n👤 Contact Found")
            print(f"Name  : {contact['name']}")
            print(f"Phone : {number}")
            print(f"Email : {contact['email'] or 'Not provided'}")

            found = True

    if not found:
        print("❌ No matching contact found.")


def update_contact():
    phone = input("\nEnter phone number of contact: ").strip()

    if phone not in contacts:
        print("❌ Contact not found.")
        return

    contact = contacts[phone]

    print("\nLeave a field empty to keep the existing value.")

    new_name = input(f"Name [{contact['name']}]: ").strip()
    new_email = input(f"Email [{contact['email']}]: ").strip()

    if new_name:
        contact["name"] = new_name.title()

    if new_email:
        contact["email"] = new_email.lower()

    print("✅ Contact updated successfully!")


def delete_contact():
    phone = input("\nEnter phone number to delete: ").strip()

    if phone not in contacts:
        print("❌ Contact not found.")
        return

    removed = contacts.pop(phone)

    print(f"🗑️ Deleted contact: {removed['name']}")


def contact_summary():
    print("\n--- 📊 Contact Summary ---")
    print(f"Total Contacts: {len(contacts)}")


def show_menu():
    print("\n" + "=" * 45)
    print("           📒 CONTACT BOOK")
    print("=" * 45)

    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Contact Summary")
    print("7. Exit")


while True:

    show_menu()

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        contact_summary()

    elif choice == "7":
        print("\n👋 Contact Book closed.")
        break

    else:
        print("❌ Invalid choice. Please select 1-7.")