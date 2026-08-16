tasks = []


def add_task():
    print("\n--- ➕ Add Task ---")

    title = input("Enter task: ").strip()

    if not title:
        print("❌ Task cannot be empty.")
        return

    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)

    print("✅ Task added successfully!")


def view_tasks():
    print("\n--- 📋 Your Tasks ---")

    if not tasks:
        print("📭 No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):

        if task["completed"]:
            status = "✅ Completed"
        else:
            status = "⏳ Pending"

        print(f"{index}. {task['title']} — {status}")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to complete: "))

        if 1 <= number <= len(tasks):

            task = tasks[number - 1]

            if task["completed"]:
                print("ℹ️ Task is already completed.")
            else:
                task["completed"] = True
                print("✅ Task marked as completed!")

        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to delete: "))

        if 1 <= number <= len(tasks):

            removed = tasks.pop(number - 1)

            print(f"🗑️ Deleted task: {removed['title']}")

        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")


def search_task():
    keyword = input("\nEnter keyword to search: ").strip().lower()

    found = False

    print("\n--- 🔍 Search Results ---")

    for index, task in enumerate(tasks, start=1):

        if keyword in task["title"].lower():

            status = (
                "✅ Completed"
                if task["completed"]
                else "⏳ Pending"
            )

            print(f"{index}. {task['title']} — {status}")
            found = True

    if not found:
        print("❌ No matching tasks found.")


def task_summary():
    completed = 0
    pending = 0

    for task in tasks:

        if task["completed"]:
            completed += 1
        else:
            pending += 1

    print("\n--- 📊 Task Summary ---")
    print(f"Total Tasks     : {len(tasks)}")
    print(f"Completed Tasks : {completed}")
    print(f"Pending Tasks   : {pending}")


def show_menu():
    print("\n" + "=" * 50)
    print("             ✅ TO-DO LIST MANAGER")
    print("=" * 50)

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Task Summary")
    print("7. Exit")


while True:

    show_menu()

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        search_task()

    elif choice == "6":
        task_summary()

    elif choice == "7":
        print("\n👋 Goodbye! Stay productive!")
        break

    else:
        print("❌ Invalid choice. Please select 1-7.")