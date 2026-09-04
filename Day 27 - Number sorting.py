import tkinter as tk
from tkinter import messagebox, ttk


class NumberSorter:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Number Sorter")
        self.root.geometry("950x650")
        self.root.configure(bg="#111827")

        self.numbers = []
        self.sorting = False
        self.paused = False

        self.i = 0
        self.j = 0
        self.comparisons = 0
        self.swaps = 0

        self.create_ui()

    # -------------------------
    # UI
    # -------------------------
    def create_ui(self):

        title = tk.Label(
            self.root,
            text="🔢 Real-Time Number Sorter",
            font=("Segoe UI", 26, "bold"),
            bg="#111827",
            fg="white"
        )
        title.pack(pady=(25, 5))

        subtitle = tk.Label(
            self.root,
            text="Enter numbers and watch Bubble Sort work!",
            font=("Segoe UI", 11),
            bg="#111827",
            fg="#9ca3af"
        )
        subtitle.pack(pady=(0, 20))

        # Input section
        input_frame = tk.Frame(
            self.root,
            bg="#1f2937",
            padx=15,
            pady=15
        )
        input_frame.pack(fill="x", padx=30)

        tk.Label(
            input_frame,
            text="Enter numbers:",
            font=("Segoe UI", 11, "bold"),
            bg="#1f2937",
            fg="white"
        ).pack(side="left", padx=5)

        self.input_entry = tk.Entry(
            input_frame,
            font=("Segoe UI", 11),
            width=45,
            bg="#374151",
            fg="white",
            insertbackground="white",
            relief="flat"
        )
        self.input_entry.pack(side="left", padx=10, ipady=7)

        self.input_entry.insert(
            0,
            "45, 12, 78, 23, 9, 56"
        )

        tk.Button(
            input_frame,
            text="▶ Sort",
            command=self.start_sorting,
            bg="#16a34a",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            padx=20,
            pady=8,
            cursor="hand2"
        ).pack(side="left", padx=5)

        tk.Button(
            input_frame,
            text="↻ Reset",
            command=self.reset,
            bg="#475569",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            padx=20,
            pady=8,
            cursor="hand2"
        ).pack(side="left", padx=5)

        # Controls
        controls = tk.Frame(
            self.root,
            bg="#111827"
        )
        controls.pack(fill="x", padx=30, pady=15)

        self.pause_button = tk.Button(
            controls,
            text="⏸ Pause",
            command=self.toggle_pause,
            bg="#f59e0b",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            padx=20,
            pady=8
        )
        self.pause_button.pack(side="left")

        tk.Label(
            controls,
            text="Speed:",
            bg="#111827",
            fg="white",
            font=("Segoe UI", 10, "bold")
        ).pack(side="left", padx=(30, 5))

        self.speed = ttk.Scale(
            controls,
            from_=20,
            to=500,
            orient="horizontal"
        )
        self.speed.set(120)
        self.speed.pack(side="left", padx=5)

        # Canvas
        self.canvas = tk.Canvas(
            self.root,
            bg="#0f172a",
            highlightthickness=0
        )
        self.canvas.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=10
        )

        # Stats
        stats = tk.Frame(
            self.root,
            bg="#111827"
        )
        stats.pack(
            fill="x",
            padx=30,
            pady=(5, 20)
        )

        self.comparison_label = tk.Label(
            stats,
            text="Comparisons: 0",
            font=("Segoe UI", 11, "bold"),
            bg="#111827",
            fg="#60a5fa"
        )
        self.comparison_label.pack(side="left")

        self.swap_label = tk.Label(
            stats,
            text="Swaps: 0",
            font=("Segoe UI", 11, "bold"),
            bg="#111827",
            fg="#34d399"
        )
        self.swap_label.pack(side="left", padx=40)

        self.status_label = tk.Label(
            stats,
            text="Enter numbers to begin",
            font=("Segoe UI", 11),
            bg="#111827",
            fg="#9ca3af"
        )
        self.status_label.pack(side="right")

    # -------------------------
    # Read User Input
    # -------------------------
    def get_numbers(self):

        user_input = self.input_entry.get().strip()

        if not user_input:
            messagebox.showerror(
                "Input Error",
                "Please enter some numbers."
            )
            return False

        try:
            self.numbers = [
                int(num.strip())
                for num in user_input.split(",")
            ]

            if len(self.numbers) < 2:
                messagebox.showerror(
                    "Input Error",
                    "Please enter at least two numbers."
                )
                return False

            return True

        except ValueError:
            messagebox.showerror(
                "Input Error",
                "Please enter valid numbers separated by commas."
            )
            return False

    # -------------------------
    # Start Sorting
    # -------------------------
    def start_sorting(self):

        if self.sorting:
            return

        if not self.get_numbers():
            return

        self.sorting = True
        self.paused = False

        self.i = 0
        self.j = 0
        self.comparisons = 0
        self.swaps = 0

        self.pause_button.config(
            text="⏸ Pause"
        )

        self.status_label.config(
            text="Sorting..."
        )

        self.update_stats()
        self.draw_numbers()

        self.sort_step()

    # -------------------------
    # Pause / Resume
    # -------------------------
    def toggle_pause(self):

        if not self.sorting:
            return

        self.paused = not self.paused

        if self.paused:

            self.pause_button.config(
                text="▶ Resume"
            )

            self.status_label.config(
                text="Paused"
            )

        else:

            self.pause_button.config(
                text="⏸ Pause"
            )

            self.status_label.config(
                text="Sorting..."
            )

            self.sort_step()

    # -------------------------
    # Bubble Sort Animation
    # -------------------------
    def sort_step(self):

        if not self.sorting or self.paused:
            return

        n = len(self.numbers)

        # Sorting complete
        if self.i >= n - 1:

            self.sorting = False

            self.status_label.config(
                text="✅ Sorting completed!"
            )

            self.draw_numbers()

            return

        # Current pass complete
        if self.j >= n - self.i - 1:

            self.j = 0
            self.i += 1

            self.root.after(
                int(self.speed.get()),
                self.sort_step
            )

            return

        # Comparison
        self.comparisons += 1

        # Swap
        if self.numbers[self.j] > self.numbers[self.j + 1]:

            self.numbers[self.j], self.numbers[self.j + 1] = (
                self.numbers[self.j + 1],
                self.numbers[self.j]
            )

            self.swaps += 1

        self.draw_numbers(
            active_index=self.j
        )

        self.update_stats()

        self.j += 1

        self.root.after(
            int(self.speed.get()),
            self.sort_step
        )

    # -------------------------
    # Draw Numbers
    # -------------------------
    def draw_numbers(self, active_index=None):

        self.canvas.delete("all")

        if not self.numbers:
            return

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        if width <= 1:
            width = 890

        if height <= 1:
            height = 400

        bar_width = width / len(self.numbers)

        max_value = max(self.numbers)

        # Handle negative numbers safely
        min_value = min(self.numbers)

        if min_value < 0:
            offset = abs(min_value)
            values = [
                value + offset
                for value in self.numbers
            ]
            max_value = max(values)
        else:
            values = self.numbers

        for index, value in enumerate(self.numbers):

            display_value = values[index]

            if max_value == 0:
                bar_height = 20
            else:
                bar_height = (
                    display_value / max_value
                ) * (height - 80)

            x1 = index * bar_width + 4
            y1 = height - bar_height - 10

            x2 = (index + 1) * bar_width - 4
            y2 = height - 10

            # Highlight numbers currently being compared
            if (
                active_index is not None
                and (
                    index == active_index
                    or index == active_index + 1
                )
            ):
                bar_color = "#f97316"
            else:
                bar_color = "#3b82f6"

            self.canvas.create_rectangle(
                x1,
                y1,
                x2,
                y2,
                fill=bar_color,
                outline=""
            )

            self.canvas.create_text(
                (x1 + x2) / 2,
                y1 - 12,
                text=str(value),
                fill="#cbd5e1",
                font=("Segoe UI", 9)
            )

    # -------------------------
    # Update Statistics
    # -------------------------
    def update_stats(self):

        self.comparison_label.config(
            text=f"Comparisons: {self.comparisons}"
        )

        self.swap_label.config(
            text=f"Swaps: {self.swaps}"
        )

    # -------------------------
    # Reset
    # -------------------------
    def reset(self):

        self.sorting = False
        self.paused = False

        self.numbers = []

        self.i = 0
        self.j = 0

        self.comparisons = 0
        self.swaps = 0

        self.pause_button.config(
            text="⏸ Pause"
        )

        self.status_label.config(
            text="Enter numbers to begin"
        )

        self.update_stats()

        self.canvas.delete("all")


# -------------------------
# Run Application
# -------------------------

if __name__ == "__main__":

    root = tk.Tk()

    app = NumberSorter(root)

    root.mainloop()