import random
import time


sentences = [
    "Python is a powerful programming language.",
    "Practice makes programming skills better.",
    "Consistency is the key to learning coding.",
    "Build projects to improve your programming skills.",
    "Every developer starts by writing simple programs."
]


def calculate_accuracy(original, typed):
    correct = 0

    for i in range(min(len(original), len(typed))):
        if original[i] == typed[i]:
            correct += 1

    if len(original) == 0:
        return 0

    return (correct / len(original)) * 100


def typing_test():

    sentence = random.choice(sentences)

    print("=" * 60)
    print("             ⌨️ TYPING SPEED TEST")
    print("=" * 60)

    print("\nType the following sentence:\n")

    print(f'"{sentence}"')

    input("\nPress ENTER when you're ready...")

    print("\n🚀 START TYPING!")

    start_time = time.time()

    typed_text = input("\n> ")

    end_time = time.time()

    time_taken = end_time - start_time

    words = len(typed_text.split())

    minutes = time_taken / 60

    if minutes > 0:
        wpm = words / minutes
    else:
        wpm = 0

    accuracy = calculate_accuracy(
        sentence,
        typed_text
    )

    mistakes = abs(
        len(sentence) - len(typed_text)
    )

    print("\n" + "=" * 50)
    print("             📊 YOUR RESULTS")
    print("=" * 50)

    print(f"⏱️ Time Taken : {time_taken:.2f} seconds")
    print(f"⚡ Speed      : {wpm:.2f} WPM")
    print(f"🎯 Accuracy   : {accuracy:.2f}%")
    print(f"❌ Mistakes   : {mistakes}")

    if accuracy >= 95:
        print("🏆 Excellent!")

    elif accuracy >= 85:
        print("🔥 Very Good!")

    elif accuracy >= 70:
        print("👍 Good! Keep practicing.")

    else:
        print("📚 Keep practicing!")


def main():

    while True:

        typing_test()

        again = input(
            "\n🔄 Try again? (y/n): "
        ).lower()

        if again != "y":
            print("\n👋 Thanks for playing!")
            break


main()