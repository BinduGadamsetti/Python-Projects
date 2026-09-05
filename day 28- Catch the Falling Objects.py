import tkinter as tk
import random


class CatchGame:

    def __init__(self, root):

        self.root = root
        self.root.title("Catch the Falling Objects")
        self.root.geometry("800x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#111827")

        # Game settings
        self.canvas_width = 800
        self.canvas_height = 500

        self.basket_width = 100
        self.basket_height = 20

        self.object_size = 30

        # Game variables
        self.score = 0
        self.lives = 3
        self.high_score = 0

        self.basket_x = 350
        self.basket_y = 450

        self.object_x = 0
        self.object_y = 0

        self.object_speed = 5

        self.game_running = False
        self.game_loop_id = None

        self.create_ui()

    # =================================
    # UI
    # =================================

    def create_ui(self):

        title = tk.Label(
            self.root,
            text="🎮 Catch the Falling Objects",
            font=("Segoe UI", 24, "bold"),
            bg="#111827",
            fg="white"
        )
        title.pack(pady=15)

        # Score area
        info = tk.Frame(
            self.root,
            bg="#111827"
        )
        info.pack(fill="x", padx=30)

        self.score_label = tk.Label(
            info,
            text="Score: 0",
            font=("Segoe UI", 12, "bold"),
            bg="#111827",
            fg="#60a5fa"
        )
        self.score_label.pack(side="left")

        self.lives_label = tk.Label(
            info,
            text="❤️ Lives: 3",
            font=("Segoe UI", 12, "bold"),
            bg="#111827",
            fg="#f87171"
        )
        self.lives_label.pack(side="left", padx=40)

        self.high_score_label = tk.Label(
            info,
            text="🏆 High Score: 0",
            font=("Segoe UI", 12, "bold"),
            bg="#111827",
            fg="#fbbf24"
        )
        self.high_score_label.pack(side="right")

        # Canvas
        self.canvas = tk.Canvas(
            self.root,
            width=self.canvas_width,
            height=self.canvas_height,
            bg="#0f172a",
            highlightthickness=0
        )
        self.canvas.pack(pady=15)

        # Basket
        self.basket = self.canvas.create_rectangle(
            self.basket_x,
            self.basket_y,
            self.basket_x + self.basket_width,
            self.basket_y + self.basket_height,
            fill="#3b82f6",
            outline=""
        )

        # Falling object
        self.falling_object = self.canvas.create_oval(
            0,
            0,
            self.object_size,
            self.object_size,
            fill="#f97316",
            outline=""
        )

        # Start button
        self.start_button = tk.Button(
            self.root,
            text="▶ Start Game",
            command=self.start_game,
            font=("Segoe UI", 11, "bold"),
            bg="#16a34a",
            fg="white",
            relief="flat",
            padx=25,
            pady=8,
            cursor="hand2"
        )
        self.start_button.pack()

        # Instructions
        tk.Label(
            self.root,
            text="Use ← → arrow keys to move the basket",
            font=("Segoe UI", 10),
            bg="#111827",
            fg="#9ca3af"
        ).pack(pady=8)

        # Keyboard controls
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        # Hide object initially
        self.canvas.itemconfig(
            self.falling_object,
            state="hidden"
        )

    # =================================
    # Start / Restart Game
    # =================================

    def start_game(self):

        # Cancel previous game loop
        if self.game_loop_id is not None:

            try:
                self.root.after_cancel(
                    self.game_loop_id
                )
            except:
                pass

            self.game_loop_id = None

        # Remove old game-over text
        self.canvas.delete("game_over")

        # Reset values
        self.score = 0
        self.lives = 3
        self.object_speed = 5

        self.basket_x = (
            self.canvas_width - self.basket_width
        ) // 2

        self.game_running = True

        # Move basket to center
        self.canvas.coords(
            self.basket,
            self.basket_x,
            self.basket_y,
            self.basket_x + self.basket_width,
            self.basket_y + self.basket_height
        )

        self.update_labels()

        self.start_button.config(
            text="🔄 Restart Game"
        )

        self.create_object()

        # Start ONE game loop
        self.game_loop()

    # =================================
    # Create New Object
    # =================================

    def create_object(self):

        self.object_x = random.randint(
            0,
            self.canvas_width - self.object_size
        )

        self.object_y = -self.object_size

        self.canvas.coords(
            self.falling_object,
            self.object_x,
            self.object_y,
            self.object_x + self.object_size,
            self.object_y + self.object_size
        )

        self.canvas.itemconfig(
            self.falling_object,
            state="normal"
        )

    # =================================
    # Move Left
    # =================================

    def move_left(self, event=None):

        if not self.game_running:
            return

        self.basket_x -= 30

        if self.basket_x < 0:
            self.basket_x = 0

        self.update_basket()

    # =================================
    # Move Right
    # =================================

    def move_right(self, event=None):

        if not self.game_running:
            return

        self.basket_x += 30

        if (
            self.basket_x + self.basket_width
            > self.canvas_width
        ):
            self.basket_x = (
                self.canvas_width
                - self.basket_width
            )

        self.update_basket()

    # =================================
    # Update Basket
    # =================================

    def update_basket(self):

        self.canvas.coords(
            self.basket,
            self.basket_x,
            self.basket_y,
            self.basket_x + self.basket_width,
            self.basket_y + self.basket_height
        )

    # =================================
    # Game Loop
    # =================================

    def game_loop(self):

        if not self.game_running:
            return

        # Move object
        self.object_y += self.object_speed

        self.canvas.coords(
            self.falling_object,
            self.object_x,
            self.object_y,
            self.object_x + self.object_size,
            self.object_y + self.object_size
        )

        # Check collision
        if self.check_collision():

            self.score += 1

            # Increase difficulty every 5 points
            if self.score % 5 == 0:
                self.object_speed += 1

            self.update_labels()

            self.create_object()

        # Object reached bottom
        elif self.object_y > self.canvas_height:

            self.lives -= 1

            self.update_labels()

            if self.lives <= 0:

                self.game_over()
                return

            self.create_object()

        # Continue game
        self.game_loop_id = self.root.after(
            30,
            self.game_loop
        )

    # =================================
    # Collision Detection
    # =================================

    def check_collision(self):

        object_left = self.object_x
        object_right = (
            self.object_x + self.object_size
        )

        object_bottom = (
            self.object_y + self.object_size
        )

        basket_left = self.basket_x
        basket_right = (
            self.basket_x + self.basket_width
        )

        basket_top = self.basket_y

        return (
            object_bottom >= basket_top
            and object_left <= basket_right
            and object_right >= basket_left
        )

    # =================================
    # Game Over
    # =================================

    def game_over(self):

        self.game_running = False

        if self.game_loop_id is not None:

            try:
                self.root.after_cancel(
                    self.game_loop_id
                )
            except:
                pass

            self.game_loop_id = None

        # Update high score
        if self.score > self.high_score:

            self.high_score = self.score

        self.update_labels()

        self.canvas.itemconfig(
            self.falling_object,
            state="hidden"
        )

        self.canvas.create_text(
            self.canvas_width / 2,
            self.canvas_height / 2,
            text=f"GAME OVER\n\nScore: {self.score}",
            fill="white",
            font=("Segoe UI", 30, "bold"),
            justify="center",
            tags="game_over"
        )

    # =================================
    # Update Labels
    # =================================

    def update_labels(self):

        self.score_label.config(
            text=f"Score: {self.score}"
        )

        self.lives_label.config(
            text=f"❤️ Lives: {self.lives}"
        )

        self.high_score_label.config(
            text=f"🏆 High Score: {self.high_score}"
        )


# =====================================
# Run Game
# =====================================

if __name__ == "__main__":

    root = tk.Tk()

    game = CatchGame(root)

    root.mainloop()