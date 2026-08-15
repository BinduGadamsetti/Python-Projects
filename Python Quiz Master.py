import random

questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. def", "C. function", "D. define"],
        "answer": "B"
    },
    {
        "question": "Which data type is immutable?",
        "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
        "answer": "D"
    },
    {
        "question": "What does len() return?",
        "options": [
            "A. Data type",
            "B. Length of an object",
            "C. Memory size",
            "D. Index"
        ],
        "answer": "B"
    },
    {
        "question": "Which operator is used for exponentiation?",
        "options": ["A. ^", "B. //", "C. **", "D. %%"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to handle exceptions?",
        "options": ["A. error", "B. catch", "C. try", "D. handle"],
        "answer": "C"
    },
    {
        "question": "Which collection stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
        "answer": "D"
    },
    {
        "question": "What is the output of 10 // 3?",
        "options": ["A. 3.33", "B. 3", "C. 1", "D. 4"],
        "answer": "B"
    },
    {
        "question": "Which function converts a string to an integer?",
        "options": ["A. str()", "B. float()", "C. int()", "D. number()"],
        "answer": "C"
    }
]


def display_question(number, question):
    print("\n" + "-" * 55)
    print(f"Question {number}: {question['question']}")
    print("-" * 55)

    for option in question["options"]:
        print(option)


def get_answer():
    while True:
        answer = input("\nYour answer (A/B/C/D): ").strip().upper()

        if answer in ["A", "B", "C", "D"]:
            return answer

        print("❌ Invalid choice. Please enter A, B, C, or D.")


def calculate_result(score, total):
    percentage = (score / total) * 100

    if percentage >= 90:
        rating = "🏆 Excellent!"
    elif percentage >= 75:
        rating = "🥇 Very Good!"
    elif percentage >= 60:
        rating = "🥈 Good!"
    elif percentage >= 40:
        rating = "📚 Keep Practicing!"
    else:
        rating = "💪 Time to revise Python!"

    return percentage, rating


def start_quiz():
    score = 0

    quiz_questions = questions.copy()
    random.shuffle(quiz_questions)

    print("=" * 55)
    print("              🧠 PYTHON QUIZ MASTER")
    print("=" * 55)

    print(f"\nYou have {len(quiz_questions)} questions.")
    print("Choose the correct option: A, B, C, or D.")

    for number, question in enumerate(quiz_questions, start=1):

        display_question(number, question)

        user_answer = get_answer()

        if user_answer == question["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(
                f"❌ Incorrect! "
                f"The correct answer was {question['answer']}."
            )

    percentage, rating = calculate_result(
        score,
        len(quiz_questions)
    )

    print("\n" + "=" * 55)
    print("                📊 FINAL RESULT")
    print("=" * 55)

    print(f"Correct Answers : {score}")
    print(f"Wrong Answers   : {len(quiz_questions) - score}")
    print(f"Score           : {score}/{len(quiz_questions)}")
    print(f"Percentage      : {percentage:.2f}%")
    print(f"Performance     : {rating}")

    print("=" * 55)


start_quiz()