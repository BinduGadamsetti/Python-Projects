print("=" * 45)
print("          🧮 SMART CALCULATOR")
print("=" * 45)

while True:
    try:
        num1 = float(input("\nEnter first number: "))
        operator = input(
            "Choose operation (+, -, *, /, //, %, **, %%) : "
        ).strip()
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":
            if num2 == 0:
                print("❌ Cannot divide by zero!")
                continue
            result = num1 / num2

        elif operator == "//":
            if num2 == 0:
                print("❌ Cannot divide by zero!")
                continue
            result = num1 // num2

        elif operator == "%":
            if num2 == 0:
                print("❌ Cannot divide by zero!")
                continue
            result = num1 % num2

        elif operator == "**":
            result = num1 ** num2

        elif operator == "%%":
            result = (num1 * num2) / 100

        else:
            print("❌ Invalid operator!")
            continue

        print(f"\n✅ Result: {result}")

    except ValueError:
        print("❌ Please enter valid numbers.")

    again = input("\nDo you want to calculate again? (yes/no): ").lower()

    if again != "yes":
        print("\n👋 Calculator closed. Keep coding!")
        break