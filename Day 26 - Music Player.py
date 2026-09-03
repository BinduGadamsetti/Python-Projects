import tkinter as tk
from tkinter import messagebox


# ============================================================
#                    DOUBLY LINKED LIST
# ============================================================

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.previous = None
        self.next = None


class Playlist:

    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    # ---------------- ADD SONG ----------------

    def add_song(self, title, artist):

        new_song = Song(title, artist)

        if self.head is None:
            self.head = new_song
            self.tail = new_song
            self.current = new_song

        else:
            new_song.previous = self.tail
            self.tail.next = new_song
            self.tail = new_song

    # ---------------- REMOVE SONG ----------------

    def remove_song(self, title):

        current = self.head

        while current:

            if current.title.lower() == title.lower():

                if current.previous:
                    current.previous.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.previous = current.previous
                else:
                    self.tail = current.previous

                if self.current == current:

                    if current.next:
                        self.current = current.next
                    elif current.previous:
                        self.current = current.previous
                    else:
                        self.current = None

                return True

            current = current.next

        return False

    # ---------------- SEARCH SONG ----------------

    def search_song(self, title):

        current = self.head

        while current:

            if current.title.lower() == title.lower():
                return current

            current = current.next

        return None

    # ---------------- NEXT ----------------

    def next_song(self):

        if self.current and self.current.next:

            self.current = self.current.next
            return self.current

        return None

    # ---------------- PREVIOUS ----------------

    def previous_song(self):

        if self.current and self.current.previous:

            self.current = self.current.previous
            return self.current

        return None

    # ---------------- FIRST ----------------

    def first_song(self):

        if self.head:
            self.current = self.head
            return self.current

        return None

    # ---------------- LAST ----------------

    def last_song(self):

        if self.tail:
            self.current = self.tail
            return self.current

        return None

    # ---------------- COUNT ----------------

    def count(self):

        total = 0
        current = self.head

        while current:
            total += 1
            current = current.next

        return total


# ============================================================
#                    GUI APPLICATION
# ============================================================

class MusicPlayer:

    def __init__(self, root):

        self.root = root
        self.root.title("🎵 Music Playlist Manager")
        self.root.geometry("850x650")
        self.root.resizable(False, False)

        self.playlist = Playlist()

        # ---------------- GRADIENT BACKGROUND ----------------

        self.canvas = tk.Canvas(
            root,
            width=850,
            height=650,
            highlightthickness=0
        )

        self.canvas.pack(fill="both", expand=True)

        self.create_gradient()

        # ---------------- MAIN CONTAINER ----------------

        self.main_frame = tk.Frame(
            root,
            bg="#ffffff"
        )

        self.main_frame.place(
            x=75,
            y=40,
            width=700,
            height=570
        )

        # ---------------- TITLE ----------------

        title = tk.Label(
            self.main_frame,
            text="🎵 Music Playlist",
            font=("Arial", 26, "bold"),
            bg="#ffffff",
            fg="#5b2c83"
        )

        title.pack(pady=(20, 5))

        subtitle = tk.Label(
            self.main_frame,
            text="Your playlist • Your music • Your vibe",
            font=("Arial", 11),
            bg="#ffffff",
            fg="#777777"
        )

        subtitle.pack(pady=(0, 15))

        # ---------------- INPUT FRAME ----------------

        input_frame = tk.Frame(
            self.main_frame,
            bg="#ffffff"
        )

        input_frame.pack(pady=5)

        self.title_entry = tk.Entry(
            input_frame,
            font=("Arial", 12),
            width=23,
            relief="solid",
            bd=1
        )

        self.title_entry.grid(
            row=0,
            column=0,
            padx=5,
            ipady=7
        )

        self.title_entry.insert(
            0,
            "Song title"
        )

        self.artist_entry = tk.Entry(
            input_frame,
            font=("Arial", 12),
            width=23,
            relief="solid",
            bd=1
        )

        self.artist_entry.grid(
            row=0,
            column=1,
            padx=5,
            ipady=7
        )

        self.artist_entry.insert(
            0,
            "Artist"
        )

        add_button = tk.Button(
            input_frame,
            text="➕ Add",
            command=self.add_song,
            bg="#e75480",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            padx=15,
            pady=7,
            cursor="hand2"
        )

        add_button.grid(
            row=0,
            column=2,
            padx=5
        )

        # ---------------- SEARCH ----------------

        search_frame = tk.Frame(
            self.main_frame,
            bg="#ffffff"
        )

        search_frame.pack(
            pady=15
        )

        self.search_entry = tk.Entry(
            search_frame,
            font=("Arial", 11),
            width=38,
            relief="solid",
            bd=1
        )

        self.search_entry.pack(
            side="left",
            ipady=6
        )

        search_button = tk.Button(
            search_frame,
            text="🔍 Search",
            command=self.search_song,
            bg="#5b7cfa",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            padx=12,
            pady=6,
            cursor="hand2"
        )

        search_button.pack(
            side="left",
            padx=5
        )

        # ---------------- PLAYLIST ----------------

        playlist_frame = tk.Frame(
            self.main_frame,
            bg="#f7f7ff",
            bd=1,
            relief="solid"
        )

        playlist_frame.pack(
            padx=35,
            fill="both",
            expand=True
        )

        playlist_label = tk.Label(
            playlist_frame,
            text="📋 YOUR PLAYLIST",
            font=("Arial", 11, "bold"),
            bg="#f7f7ff",
            fg="#5b2c83"
        )

        playlist_label.pack(
            anchor="w",
            padx=15,
            pady=10
        )

        list_container = tk.Frame(
            playlist_frame,
            bg="#f7f7ff"
        )

        list_container.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 10)
        )

        scrollbar = tk.Scrollbar(
            list_container
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.song_list = tk.Listbox(
            list_container,
            font=("Arial", 12),
            bg="#ffffff",
            fg="#333333",
            selectbackground="#e75480",
            selectforeground="white",
            activestyle="none",
            yscrollcommand=scrollbar.set,
            relief="flat"
        )

        self.song_list.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.config(
            command=self.song_list.yview
        )

        # ---------------- CONTROL BUTTONS ----------------

        control_frame = tk.Frame(
            self.main_frame,
            bg="#ffffff"
        )

        control_frame.pack(
            pady=12
        )

        buttons = [
            ("⏮️", self.previous_song),
            ("▶️", self.play_song),
            ("⏭️", self.next_song),
            ("🗑️", self.remove_song)
        ]

        for text, command in buttons:

            button = tk.Button(
                control_frame,
                text=text,
                command=command,
                font=("Arial", 16),
                bg="#eef0ff",
                fg="#5b2c83",
                relief="flat",
                width=5,
                height=1,
                cursor="hand2"
            )

            button.pack(
                side="left",
                padx=6
            )

        # ---------------- STATUS ----------------

        self.now_playing = tk.Label(
            self.main_frame,
            text="🎧 Nothing playing",
            font=("Arial", 11, "bold"),
            bg="#ffffff",
            fg="#e75480"
        )

        self.now_playing.pack(
            pady=(0, 8)
        )

        self.status = tk.Label(
            self.main_frame,
            text="🎵 0 songs",
            font=("Arial", 10),
            bg="#ffffff",
            fg="#777777"
        )

        self.status.pack(
            pady=(0, 10)
        )

    # ========================================================
    #                    GRADIENT
    # ========================================================

    def create_gradient(self):

        width = 850
        height = 650

        start_color = (255, 182, 193)   # Pink
        end_color = (135, 206, 250)     # Blue

        for i in range(height):

            ratio = i / height

            r = int(
                start_color[0]
                + (end_color[0] - start_color[0]) * ratio
            )

            g = int(
                start_color[1]
                + (end_color[1] - start_color[1]) * ratio
            )

            b = int(
                start_color[2]
                + (end_color[2] - start_color[2]) * ratio
            )

            color = f"#{r:02x}{g:02x}{b:02x}"

            self.canvas.create_line(
                0,
                i,
                width,
                i,
                fill=color
            )

    # ========================================================
    #                    ADD SONG
    # ========================================================

    def add_song(self):

        title = self.title_entry.get().strip()
        artist = self.artist_entry.get().strip()

        if (
            not title
            or title == "Song title"
            or not artist
            or artist == "Artist"
        ):

            messagebox.showwarning(
                "Missing Information",
                "Please enter both song title and artist."
            )

            return

        self.playlist.add_song(
            title,
            artist
        )

        self.title_entry.delete(
            0,
            tk.END
        )

        self.artist_entry.delete(
            0,
            tk.END
        )

        self.refresh_playlist()

    # ========================================================
    #                    REMOVE SONG
    # ========================================================

    def remove_song(self):

        selection = self.song_list.curselection()

        if not selection:

            messagebox.showinfo(
                "Select Song",
                "Please select a song to remove."
            )

            return

        index = selection[0]

        current = self.playlist.head

        for _ in range(index):
            current = current.next

        title = current.title

        self.playlist.remove_song(
            title
        )

        self.refresh_playlist()

        self.now_playing.config(
            text="🎧 Nothing playing"
        )

    # ========================================================
    #                    PLAY SONG
    # ========================================================

    def play_song(self):

        selection = self.song_list.curselection()

        if not selection:

            if self.playlist.current is None:

                messagebox.showinfo(
                    "Playlist Empty",
                    "Please add a song first."
                )

                return

            current = self.playlist.current

        else:

            index = selection[0]

            current = self.playlist.head

            for _ in range(index):
                current = current.next

            self.playlist.current = current

        self.now_playing.config(
            text=f"▶️ Now Playing: "
                 f"{current.title} — {current.artist}"
        )

        self.refresh_playlist()

    # ========================================================
    #                    NEXT SONG
    # ========================================================

    def next_song(self):

        if self.playlist.current is None:

            messagebox.showinfo(
                "Playlist Empty",
                "Add some songs first."
            )

            return

        song = self.playlist.next_song()

        if song:

            self.now_playing.config(
                text=f"▶️ Now Playing: "
                     f"{song.title} — {song.artist}"
            )

            self.refresh_playlist()

        else:

            messagebox.showinfo(
                "End of Playlist",
                "You are already at the last song."
            )

    # ========================================================
    #                    PREVIOUS SONG
    # ========================================================

    def previous_song(self):

        if self.playlist.current is None:

            messagebox.showinfo(
                "Playlist Empty",
                "Add some songs first."
            )

            return

        song = self.playlist.previous_song()

        if song:

            self.now_playing.config(
                text=f"▶️ Now Playing: "
                     f"{song.title} — {song.artist}"
            )

            self.refresh_playlist()

        else:

            messagebox.showinfo(
                "Start of Playlist",
                "You are already at the first song."
            )

    # ========================================================
    #                    SEARCH SONG
    # ========================================================

    def search_song(self):

        title = self.search_entry.get().strip()

        if not title:
            messagebox.showwarning(
                "Search",
                "Enter a song title."
            )
            return

        song = self.playlist.search_song(
            title
        )

        if song:

            messagebox.showinfo(
                "Song Found 🎵",
                f"Title: {song.title}\n"
                f"Artist: {song.artist}"
            )

        else:

            messagebox.showinfo(
                "Not Found",
                "Song not found in playlist."
            )

    # ========================================================
    #                    REFRESH PLAYLIST
    # ========================================================

    def refresh_playlist(self):

        self.song_list.delete(
            0,
            tk.END
        )

        current = self.playlist.head

        number = 1

        while current:

            if current == self.playlist.current:

                symbol = "▶️"

            else:

                symbol = "🎵"

            self.song_list.insert(
                tk.END,
                f"{symbol}  {number}. "
                f"{current.title} — {current.artist}"
            )

            current = current.next
            number += 1

        total = self.playlist.count()

        self.status.config(
            text=f"🎵 {total} song"
                 f"{'s' if total != 1 else ''} in playlist"
        )


# ============================================================
#                    START APPLICATION
# ============================================================

root = tk.Tk()

app = MusicPlayer(root)

root.mainloop()