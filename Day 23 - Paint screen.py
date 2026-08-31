import tkinter as tk
from tkinter import colorchooser, filedialog


class PaintApp:

    def __init__(self, root):

        self.root = root
        self.root.title("🎨 Mini Paint")
        self.root.geometry("1000x700")

        # Drawing settings
        self.color = "black"
        self.selected_color = "black"
        self.brush_size = 5

        self.last_x = None
        self.last_y = None

        # ================= TOOLBAR =================

        toolbar = tk.Frame(
            root,
            bg="#eeeeee",
            height=60
        )

        toolbar.pack(
            side=tk.TOP,
            fill=tk.X
        )

        # Brush button
        tk.Button(
            toolbar,
            text="🖌️ Brush",
            command=self.brush
        ).pack(
            side=tk.LEFT,
            padx=8,
            pady=10
        )

        # Color button
        tk.Button(
            toolbar,
            text="🎨 Color",
            command=self.choose_color
        ).pack(
            side=tk.LEFT,
            padx=8
        )

        # Eraser button
        tk.Button(
            toolbar,
            text="🧹 Eraser",
            command=self.eraser
        ).pack(
            side=tk.LEFT,
            padx=8
        )

        # Clear button
        tk.Button(
            toolbar,
            text="🗑️ Clear",
            command=self.clear_canvas
        ).pack(
            side=tk.LEFT,
            padx=8
        )

        # Save button
        tk.Button(
            toolbar,
            text="💾 Save",
            command=self.save_drawing
        ).pack(
            side=tk.LEFT,
            padx=8
        )

        # Brush size label
        tk.Label(
            toolbar,
            text="Brush Size:",
            bg="#eeeeee"
        ).pack(
            side=tk.LEFT,
            padx=(25, 5)
        )

        # Brush size slider
        self.size_slider = tk.Scale(
            toolbar,
            from_=1,
            to=30,
            orient=tk.HORIZONTAL,
            command=self.change_size,
            bg="#eeeeee"
        )

        self.size_slider.set(5)

        self.size_slider.pack(
            side=tk.LEFT
        )

        # ================= CANVAS =================

        self.canvas = tk.Canvas(
            root,
            bg="white",
            cursor="cross"
        )

        self.canvas.pack(
            fill=tk.BOTH,
            expand=True
        )

        # Mouse events
        self.canvas.bind(
            "<Button-1>",
            self.start_draw
        )

        self.canvas.bind(
            "<B1-Motion>",
            self.draw
        )

        self.canvas.bind(
            "<ButtonRelease-1>",
            self.stop_draw
        )

    # ================= DRAWING =================

    def start_draw(self, event):

        self.last_x = event.x
        self.last_y = event.y

    def draw(self, event):

        if self.last_x is not None:

            self.canvas.create_line(
                self.last_x,
                self.last_y,
                event.x,
                event.y,
                fill=self.color,
                width=self.brush_size,
                capstyle=tk.ROUND,
                smooth=True
            )

        self.last_x = event.x
        self.last_y = event.y

    def stop_draw(self, event):

        self.last_x = None
        self.last_y = None

    # ================= TOOLS =================

    def brush(self):

        # Return to previously selected color
        self.color = self.selected_color

    def choose_color(self):

        color = colorchooser.askcolor(
            title="Choose Brush Color"
        )

        if color[1]:

            self.color = color[1]
            self.selected_color = color[1]

    def eraser(self):

        # White acts as an eraser
        self.color = "white"

    def change_size(self, value):

        self.brush_size = int(value)

    def clear_canvas(self):

        self.canvas.delete("all")

    # ================= SAVE =================

    def save_drawing(self):

        filename = filedialog.asksaveasfilename(
            defaultextension=".ps",
            filetypes=[
                ("PostScript files", "*.ps")
            ]
        )

        if filename:

            self.canvas.postscript(
                file=filename,
                colormode="color"
            )

            print(
                f"✅ Drawing saved: {filename}"
            )


# ================= START APPLICATION =================

root = tk.Tk()

app = PaintApp(root)

root.mainloop()