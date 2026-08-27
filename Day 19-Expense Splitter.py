def calculate_bill(total, tip_percent, people):
    tip = total * (tip_percent / 100)
    final_amount = total + tip
    per_person = final_amount / people

    return tip, final_amount, per_person


def main():

    print("=" * 45)
    print("          💸 EXPENSE SPLITTER")
    print("=" * 45)

    try:
        total = float(input("\nEnter total bill: ₹"))
        people = int(input("Enter number of people: "))
        tip_percent = float(input("Enter tip percentage: "))

        if total <= 0 or people <= 0 or tip_percent < 0:
            print("❌ Enter valid values.")
            return

        names = []

        print("\nEnter names:")

        for i in range(people):
            name = input(f"Person {i + 1}: ").strip()
            names.append(name if name else f"Person {i + 1}")

        tip, final_amount, per_person = calculate_bill(
            total,
            tip_percent,
            people
        )

        print("\n" + "=" * 45)
        print("             🧾 BILL SUMMARY")
        print("=" * 45)

        print(f"💵 Original Bill : ₹{total:.2f}")
        print(f"💡 Tip           : ₹{tip:.2f}")
        print(f"💰 Final Bill    : ₹{final_amount:.2f}")
        print(f"👥 People        : {people}")
        print(f"💸 Each Person   : ₹{per_person:.2f}")

        print("\n👤 INDIVIDUAL SHARES")

        for name in names:
            print(f"• {name}: ₹{per_person:.2f}")

    except ValueError:
        print("❌ Please enter valid numbers.")


main()