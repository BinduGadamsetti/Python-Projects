expenses = []


def add_expense():
    print("\n--- Add Expense ---")

    category = input("Enter category: ").strip().title()

    try:
        amount = float(input("Enter amount: ₹"))

        if amount <= 0:
            print("❌ Amount must be greater than 0.")
            return

        description = input("Enter description: ").strip()

        expense = {
            "category": category,
            "amount": amount,
            "description": description
        }

        expenses.append(expense)

        print("✅ Expense added successfully!")

    except ValueError:
        print("❌ Please enter a valid amount.")


def view_expenses():
    print("\n--- All Expenses ---")

    if not expenses:
        print("📭 No expenses recorded.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['category']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['description']}"
        )


def total_expenses():
    total = sum(expense["amount"] for expense in expenses)

    print(f"\n💰 Total Spending: ₹{total:.2f}")


def category_summary():
    print("\n--- Category Summary ---")

    if not expenses:
        print("📭 No expenses recorded.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        summary[category] = summary.get(category, 0) + amount

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")


def highest_expense():
    if not expenses:
        print("\n📭 No expenses recorded.")
        return

    highest = max(expenses, key=lambda expense: expense["amount"])

    print("\n--- Highest Expense ---")
    print(f"Category    : {highest['category']}")
    print(f"Amount      : ₹{highest['amount']:.2f}")
    print(f"Description : {highest['description']}")


def delete_expense():
    view_expenses()

    if not expenses:
        return

    try:
        number = int(input("\nEnter expense number to delete: "))

        if 1 <= number <= len(expenses):
            removed = expenses.pop(number - 1)

            print(
                f"🗑️ Deleted: "
                f"{removed['category']} - ₹{removed['amount']:.2f}"
            )
        else:
            print("❌ Invalid expense number.")

    except ValueError:
        print("❌ Please enter a valid number.")


def show_menu():
    print("\n" + "=" * 45)
    print("          💰 EXPENSE TRACKER")
    print("=" * 45)

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Category Summary")
    print("5. Highest Expense")
    print("6. Delete Expense")
    print("7. Exit")


while True:

    show_menu()

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        category_summary()

    elif choice == "5":
        highest_expense()

    elif choice == "6":
        delete_expense()

    elif choice == "7":
        print("\n👋 Thank you for using Expense Tracker!")
        break

    else:
        print("❌ Invalid choice. Please select 1-7.")