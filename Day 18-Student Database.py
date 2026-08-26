import json
import os

FILE_NAME = "students.json"


def load_data():
    if not os.path.exists(FILE_NAME):
        return {}

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}


def save_data(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):

    roll = input("\nEnter roll number: ").strip()

    if roll in students:
        print("❌ Student already exists.")
        return

    name = input("Enter name: ").strip()
    branch = input("Enter branch: ").strip()
    year = input("Enter year: ").strip()

    students[roll] = {
        "name": name,
        "branch": branch,
        "year": year
    }

    save_data(students)

    print("✅ Student added successfully.")


def view_students(students):

    if not students:
        print("\n📭 No students found.")
        return

    print("\n" + "=" * 60)
    print("                 STUDENT DATABASE")
    print("=" * 60)

    for roll, student in students.items():

        print(f"""
Roll   : {roll}
Name   : {student['name']}
Branch : {student['branch']}
Year   : {student['year']}
------------------------------""")


def search_student(students):

    roll = input("\nEnter roll number: ").strip()

    if roll not in students:
        print("❌ Student not found.")
        return

    student = students[roll]

    print("\n🔍 STUDENT FOUND")
    print(f"Roll   : {roll}")
    print(f"Name   : {student['name']}")
    print(f"Branch : {student['branch']}")
    print(f"Year   : {student['year']}")


def update_student(students):

    roll = input("\nEnter roll number: ").strip()

    if roll not in students:
        print("❌ Student not found.")
        return

    print("\nLeave a field empty to keep the old value.")

    name = input(
        f"Name [{students[roll]['name']}]: "
    ).strip()

    branch = input(
        f"Branch [{students[roll]['branch']}]: "
    ).strip()

    year = input(
        f"Year [{students[roll]['year']}]: "
    ).strip()

    if name:
        students[roll]["name"] = name

    if branch:
        students[roll]["branch"] = branch

    if year:
        students[roll]["year"] = year

    save_data(students)

    print("✅ Student updated successfully.")


def delete_student(students):

    roll = input("\nEnter roll number: ").strip()

    if roll not in students:
        print("❌ Student not found.")
        return

    confirm = input(
        f"Delete {students[roll]['name']}? (y/n): "
    ).lower()

    if confirm == "y":

        del students[roll]

        save_data(students)

        print("🗑️ Student deleted.")


def main():

    students = load_data()

    while True:

        print("\n" + "=" * 45)
        print("        🗄️ STUDENT DATABASE")
        print("=" * 45)

        print("""
1. ➕ Add Student
2. 📋 View Students
3. 🔍 Search Student
4. ✏️ Update Student
5. 🗑️ Delete Student
6. 🚪 Exit
""")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            print("\n👋 Database closed.")
            break

        else:
            print("❌ Invalid choice.")


main()