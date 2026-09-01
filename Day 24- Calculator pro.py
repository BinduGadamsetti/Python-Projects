import tkinter as tk


class Calculator:

    def __init__(self, root):

        self.root = root
        self.root.title("🧮 Calculator Pro")
        self.root.geometry("400x550")
        self.root.resizable(False, False)

        self.expression = ""

        # ================= DISPLAY =================

        self.display = tk.Entry(
            root,
            font=("Arial", 28),
            justify="right",
            bd=10,
            relief=tk.RIDGE
        )

        self.display.pack(
            padx=10,
            pady=20,
            fill=tk.X,
            ipady=10
        )

        # ================= BUTTON FRAME =================

        button_frame = tk.Frame(root)
        button_frame.pack(padx=10, pady=5)

        buttons = [
            ("C", 0, 0),
            ("⌫", 0, 1),
            ("%", 0, 2),
            ("/", 0, 3),

            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("*", 1, 3),

            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("-", 2, 3),

            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("+", 3, 3),

            ("0", 4, 0),
            (".", 4, 1),
            ("=", 4, 2),
        ]

        for text, row, column in buttons:

            button = tk.Button(
                button_frame,
                text=text,
                font=("Arial", 18, "bold"),
                width=5,
                height=2,
                command=lambda value=text:
                    self.button_click(value)
            )

            button.grid(
                row=row,
                column=column,
                padx=5,
                pady=5
            )

        # ================= KEYBOARD =================

        self.root.bind(
            "<Key>",
            self.keyboard_input
        )

    # ================= BUTTON CLICK =================

    def button_click(self, value):

        if value == "C":
            self.clear()

        elif value == "⌫":
            self.backspace()

        elif value == "=":
            self.calculate()

        elif value == "%":
            self.percentage()

        else:
            self.expression += value
            self.update_display()

    # ================= DISPLAY =================

    def update_display(self):

        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    # ================= CLEAR =================

    def clear(self):

        self.expression = ""
        self.update_display()

    # ================= BACKSPACE =================

    def backspace(self):

        self.expression = self.expression[:-1]
        self.update_display()

    # ================= CALCULATE =================

    def calculate(self):

        try:

            if not self.expression:
                return

            result = eval(
                self.expression,
                {"__builtins__": None},
                {}
            )

            self.expression = str(result)
            self.update_display()

        except ZeroDivisionError:

            self.expression = "Cannot divide by zero"
            self.update_display()

        except Exception:

            self.expression = "Error"
            self.update_display()

    # ================= PERCENTAGE =================

    def percentage(self):

        try:

            if self.expression:

                result = eval(
                    self.expression,
                    {"__builtins__": None},
                    {}
                )

                self.expression = str(result / 100)
                self.update_display()

        except Exception:

            self.expression = "Error"
            self.update_display()

    # ================= KEYBOARD INPUT =================

    def keyboard_input(self, event):

        if event.char in "0123456789+-*/.":

            self.expression += event.char
            self.update_display()

        elif event.keysym == "Return":

            self.calculate()

        elif event.keysym == "BackSpace":

            self.backspace()

        elif event.keysym == "Escape":

            self.clear()


# ================= RUN APPLICATION =================

root = tk.Tk()

calculator = Calculator(root)

root.mainloop()