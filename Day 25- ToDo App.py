import tkinter as tk
from tkinter import messagebox
import json
import os

FILE = "tasks.json"


class TodoApp:

    def __init__(self, root):
        self.root = root
        self.root.title("✅ To-Do List")
        self.root.geometry("600x650")
        self.root.resizable(False, False)

        self.tasks = []
        self.load_tasks()

        # ---------------- TITLE ----------------
        title = tk.Label(
            root,
            text="✅ My To-Do List",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=15)

        # ---------------- INPUT ----------------
        input_frame = tk.Frame(root)
        input_frame.pack(fill="x", padx=20)

        self.entry = tk.Entry(
            input_frame,
            font=("Arial", 14)
        )
        self.entry.pack(
            side="left",
            fill="x",
            expand=True,
            ipady=8
        )

        self.entry.bind(
            "<Return>",
            lambda event: self.add_task()
        )

        add_button = tk.Button(
            input_frame,
            text="➕ Add",
            font=("Arial", 12, "bold"),
            command=self.add_task
        )
        add_button.pack(
            side="left",
            padx=(8, 0),
            ipady=6
        )

        # ---------------- TASK LIST ----------------
        list_frame = tk.Frame(root)
        list_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.listbox = tk.Listbox(
            list_frame,
            font=("Arial", 14),
            height=18,
            yscrollcommand=scrollbar.set,
            selectmode=tk.SINGLE
        )

        self.listbox.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.config(
            command=self.listbox.yview
        )

        # ---------------- BUTTONS ----------------
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        complete_button = tk.Button(
            button_frame,
            text="✅ Complete",
            width=13,
            command=self.complete_task
        )
        complete_button.grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        delete_button = tk.Button(
            button_frame,
            text="🗑️ Delete",
            width=13,
            command=self.delete_task
        )
        delete_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        clear_button = tk.Button(
            button_frame,
            text="🧹 Clear Completed",
            width=16,
            command=self.clear_completed
        )
        clear_button.grid(
            row=0,
            column=2,
            padx=5,
            pady=5
        )

        save_button = tk.Button(
            button_frame,
            text="💾 Save",
            width=13,
            command=self.save_tasks
        )
        save_button.grid(
            row=1,
            column=0,
            columnspan=3,
            pady=5
        )

        # ---------------- STATUS ----------------
        self.status = tk.Label(
            root,
            text="",
            font=("Arial", 11)
        )
        self.status.pack(pady=(0, 15))

        self.refresh_tasks()

        # Save before closing
        self.root.protocol(
            "WM_DELETE_WINDOW",
            self.on_close
        )

    # ---------------- ADD TASK ----------------
    def add_task(self):

        text = self.entry.get().strip()

        if not text:
            messagebox.showwarning(
                "Empty Task",
                "Please enter a task."
            )
            return

        task = {
            "text": text,
            "completed": False
        }

        self.tasks.append(task)

        self.entry.delete(0, tk.END)

        self.save_tasks()
        self.refresh_tasks()

    # ---------------- DISPLAY TASKS ----------------
    def refresh_tasks(self):

        self.listbox.delete(0, tk.END)

        for task in self.tasks:

            if task["completed"]:
                symbol = "☑"
            else:
                symbol = "☐"

            self.listbox.insert(
                tk.END,
                f"{symbol} {task['text']}"
            )

        completed = sum(
            1 for task in self.tasks
            if task["completed"]
        )

        total = len(self.tasks)
        pending = total - completed

        self.status.config(
            text=f"Total: {total}   |   "
                 f"Completed: {completed}   |   "
                 f"Pending: {pending}"
        )

    # ---------------- COMPLETE TASK ----------------
    def complete_task(self):

        selection = self.listbox.curselection()

        if not selection:
            messagebox.showinfo(
                "Select Task",
                "Please select a task first."
            )
            return

        index = selection[0]

        self.tasks[index]["completed"] = not self.tasks[index]["completed"]

        self.save_tasks()
        self.refresh_tasks()

    # ---------------- DELETE TASK ----------------
    def delete_task(self):

        selection = self.listbox.curselection()

        if not selection:
            messagebox.showinfo(
                "Select Task",
                "Please select a task first."
            )
            return

        index = selection[0]

        del self.tasks[index]

        self.save_tasks()
        self.refresh_tasks()

    # ---------------- CLEAR COMPLETED ----------------
    def clear_completed(self):

        self.tasks = [
            task
            for task in self.tasks
            if not task["completed"]
        ]

        self.save_tasks()
        self.refresh_tasks()

    # ---------------- SAVE TASKS ----------------
    def save_tasks(self):

        try:

            with open(
                FILE,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    self.tasks,
                    file,
                    indent=4
                )

        except Exception as error:

            messagebox.showerror(
                "Save Error",
                str(error)
            )

    # ---------------- LOAD TASKS ----------------
    def load_tasks(self):

        if os.path.exists(FILE):

            try:

                with open(
                    FILE,
                    "r",
                    encoding="utf-8"
                ) as file:

                    self.tasks = json.load(file)

            except (json.JSONDecodeError, OSError):

                self.tasks = []

        else:

            self.tasks = []

    # ---------------- CLOSE APP ----------------
    def on_close(self):

        self.save_tasks()
        self.root.destroy()


# ---------------- START APPLICATION ----------------

root = tk.Tk()

app = TodoApp(root)

root.mainloop()