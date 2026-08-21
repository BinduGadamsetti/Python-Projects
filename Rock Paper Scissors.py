import random


choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0


def get_winner(player, computer):

    if player == computer:
        return "draw"

    if (
        (player == "rock" and computer == "scissors")
        or
        (player == "paper" and computer == "rock")
        or
        (player == "scissors" and computer == "paper")
    ):
        return "player"

    return "computer"


print("=" * 50)
print("        ✊ ROCK PAPER SCISSORS ✂️")
print("=" * 50)

while True:

    print("\nChoose your move:")
    print("1. ✊ Rock")
    print("2. 📄 Paper")
    print("3. ✂️ Scissors")
    print("4. 🚪 Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "4":
        break

    if choice not in ["1", "2", "3"]:
        print("❌ Invalid choice. Try again.")
        continue

    player = choices[int(choice) - 1]
    computer = random.choice(choices)

    print(f"\nYou chose     : {player.title()}")
    print(f"Computer chose: {computer.title()}")

    result = get_winner(player, computer)

    if result == "player":
        print("🎉 You Win!")
        player_score += 1

    elif result == "computer":
        print("😔 Computer Wins!")
        computer_score += 1

    else:
        print("🤝 It's a Draw!")

    print("\n📊 Score")
    print(f"You      : {player_score}")
    print(f"Computer : {computer_score}")


print("\n" + "=" * 50)
print("                 🏆 FINAL SCORE")
print("=" * 50)

print(f"You      : {player_score}")
print(f"Computer : {computer_score}")

if player_score > computer_score:
    print("🎉 Congratulations! You won the game!")

elif computer_score > player_score:
    print("😔 Computer won. Better luck next time!")

else:
    print("🤝 The game ended in a draw!")

print("\n👋 Thanks for playing!")