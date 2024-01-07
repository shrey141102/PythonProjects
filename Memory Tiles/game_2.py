import tkinter as tk
from tkinter import messagebox
import random
import time

class MemoryTile:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Memory Tiles")

        self.difficulty_var = tk.StringVar(self.parent)
        self.difficulty_var.set("Easy")

        self.difficulty_menu = tk.OptionMenu(self.parent, self.difficulty_var, "Easy", "Medium", "Hard")
        self.difficulty_menu.pack()

        self.buttons_frame = tk.Frame(self.parent)
        self.buttons_frame.pack()

        self.initialize_game()

    def initialize_game(self):
        self.create_buttons()

        self.emojis = [
            "😀", "😀", "😊", "😊", "😎", "😎", "😍", "😍",
            "🎉", "🎉", "🌟", "🌟", "🍀", "🍀", "🌈", "🌈",
            "🍕", "🍕", "🎸", "🎸", "🚀", "🚀", "🌺", "🌺",
            "🍔", "🍔", "🏆", "🏆", "🎈", "🎈", "🎁", "🎁",
            "🍟", "🍟", "🎮", "🎮", "📚", "📚", "📷", "📷",
            "🍦", "🍦", "🏰", "🏰", "🎵", "🎵", "🎨", "🎨"
        ]
        random.shuffle(self.emojis)

        difficulty = self.difficulty_var.get()
        if difficulty == "Easy":
            rows, columns = 4, 4
        elif difficulty == "Medium":
            rows, columns = 6, 6
        else:
            rows, columns = 9, 9

        self.answer = [self.emojis[i * columns:(i + 1) * columns] for i in range(rows)]

        for row in range(rows):
            for column in range(columns):
                button = tk.Button(
                    self.buttons_frame,
                    width=4,
                    height=2,
                    relief="raised",
                    bg="light gray",
                    font=("Arial", 20),
                    command=lambda row=row, column=column: self.choose_tile(row, column)
                )
                button.grid(row=row, column=column)

        self.first = None
        self.start_time = time.monotonic()
        self.center_window()

    def create_buttons(self):
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()

    def choose_tile(self, row, column):
        button = self.buttons_frame.grid_slaves(row=row, column=column)[0]
        if button["text"] == "":
            button.config(text=self.answer[row][column], bg="white")
            self.parent.update_idletasks()

            if not self.first:
                self.first = (row, column)
            else:
                x, y = self.first
                if self.answer[row][column] == self.answer[x][y]:
                    if not any("".join(row) for row in self.answer):
                        duration = time.monotonic() - self.start_time
                        message = "You win! Time: {:.1f}s\nDo you want to play again?".format(duration)
                        choice = messagebox.askyesno(title="Success!", message=message)
                        if choice:
                            self.initialize_game()
                        else:
                            self.parent.destroy()
                else:
                    self.parent.after(400, self.hide_tiles, row, column, x, y)
                self.first = None

    def hide_tiles(self, x1, y1, x2, y2):
        buttons = self.buttons_frame.grid_slaves(row=x1, column=y1)[0], self.buttons_frame.grid_slaves(row=x2, column=y2)[0]
        for button in buttons:
            button.config(text="", bg="light gray")

    def center_window(self):
        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()

        x = (screen_width - self.parent.winfo_reqwidth()) / 2
        y = (screen_height - self.parent.winfo_reqheight()) / 2 - 100

        self.parent.geometry("+%d+%d" % (x, y))


root = tk.Tk()
memory_tile = MemoryTile(root)
root.mainloop()
