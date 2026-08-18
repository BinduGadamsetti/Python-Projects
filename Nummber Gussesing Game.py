import random


def play_game():

    print("\n" + "=" * 45)
    print("        🎯 NUMBER GUESSING GAME")
    print("=" * 45)

    print("\nChoose Difficulty:")
    print("1. Easy   → 1-50, 10 attempts")
    print("2. Medium → 1-100, 7 attempts")
    print("3. Hard   → 1-200, 5 attempts")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        maximum = 50
        attempts = 10

    elif choice == "2":
        maximum = 100
        attempts = 7

    elif choice == "3":
        maximum = 200
        attempts = 5

    else:
        print("❌ Invalid choice. Starting Easy mode.")
        maximum = 50
        attempts = 10

    secret_number = random.randint(1, maximum)

    print(f"\n🎲 I selected a number between 1 and {maximum}.")
    print(f"You have {attempts} attempts!")

    for attempt in range(1, attempts + 1):

        try:
            guess = int(
                input(f"\nAttempt {attempt}/{attempts}: ")
            )

        except ValueError:
            print("❌ Please enter a number.")
            continue

        if guess < 1 or guess > maximum:
            print(f"⚠️ Enter a number between 1 and {maximum}.")
            continue

        if guess == secret_number:

            score = (attempts - attempt + 1) * 10

            print("\n🎉 Congratulations!")
            print(f"You guessed it in {attempt} attempts!")
            print(f"🏆 Your Score: {score}")

            return

        elif guess < secret_number:
            print("📈 Too Low! Try a higher number.")

        else:
            print("📉 Too High! Try a lower number.")

    print("\n😢 Game Over!")
    print(f"The number was: {secret_number}")


while True:

    play_game()

    again = input("\n🔄 Play again? (y/n): ").lower()

    if again != "y":
        print("\n👋 Thanks for playing!")
        break