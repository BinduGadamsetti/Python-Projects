# Day 15 - Digital ATM Simulator


correct_pin = "1234"
balance = 10000.0


def check_pin():
    """Verify the user's PIN."""

    for attempt in range(3):

        pin = input("🔐 Enter your 4-digit PIN: ")

        if pin == correct_pin:
            print("✅ PIN verified successfully!")
            return True

        else:
            remaining = 2 - attempt

            if remaining > 0:
                print(f"❌ Incorrect PIN. {remaining} attempt(s) left.")
            else:
                print("🔒 Too many incorrect attempts.")

    return False


def check_balance():
    """Display current account balance."""

    print(f"\n💰 Current Balance: ₹{balance:.2f}")


def deposit():
    """Deposit money into the account."""

    global balance

    try:
        amount = float(input("\nEnter deposit amount: ₹"))

        if amount <= 0:
            print("❌ Amount must be greater than zero.")
            return

        balance += amount

        print(f"✅ ₹{amount:.2f} deposited successfully.")
        print(f"💰 New Balance: ₹{balance:.2f}")

    except ValueError:
        print("❌ Please enter a valid amount.")


def withdraw():
    """Withdraw money from the account."""

    global balance

    try:
        amount = float(input("\nEnter withdrawal amount: ₹"))

        if amount <= 0:
            print("❌ Amount must be greater than zero.")
            return

        if amount > balance:
            print("❌ Insufficient balance.")
            return

        balance -= amount

        print(f"✅ Please collect ₹{amount:.2f}")
        print(f"💰 Remaining Balance: ₹{balance:.2f}")

    except ValueError:
        print("❌ Please enter a valid amount.")


def atm_menu():
    """Display ATM menu."""

    while True:

        print("\n" + "=" * 40)
        print("          🏧 ATM MENU")
        print("=" * 40)

        print("""
1. 💰 Check Balance
2. 💵 Deposit Money
3. 💸 Withdraw Money
4. 🚪 Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("\n👋 Thank you for using our ATM!")
            break

        else:
            print("❌ Invalid choice. Please select 1-4.")


def main():

    print("=" * 40)
    print("       🏧 DIGITAL ATM SIMULATOR")
    print("=" * 40)

    if check_pin():
        atm_menu()
    else:
        print("\n🚫 Account locked.")
        print("Please contact your bank.")


main()