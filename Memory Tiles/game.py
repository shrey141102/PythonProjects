import tkinter as tk
import random
from tkinter import messagebox
import time

class MemoryTile:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Memory Tiles")  # Set window title
        
        # Create a grid of buttons
        self.buttons = [
            [tk.Button(root, width=4, height=2, command=lambda row=row, column=column: self.choose_tile(row, column), font=("Arial", 20))
             for column in range(4)]
            for row in range(4)
        ]
        
        # Place buttons in the grid
        for row in range(4):
            for column in range(4):
                self.buttons[row][column].grid(row=row, column=column)
        
        self.first = None  # Variable to store the first selected tile
        self.initialize_game()  # Initialize the game
        
    def initialize_game(self):
        self.emojis = ['😈','😈','🦁','🦁','🌍','🌍','🍺','🍺','⚽','⚽','💎','💎','🐉','🐉','⏳','⏳']
        random.shuffle(self.emojis)  # Shuffle emojis for random placement
        self.answer = [self.emojis[:4], self.emojis[4:8], self.emojis[8:12], self.emojis[12:]]  # Assign emojis to grid
        
        # Reset buttons to initial state
        for row in self.buttons:
            for button in row:
                button.config(text='', state=tk.NORMAL)
        
        self.start_time = time.monotonic()  # Record the start time of the game
        self.center_window()  # Center the window on the screen
                       
    def choose_tile(self, row, column):
        self.buttons[row][column].config(text=self.answer[row][column])  # Display the selected tile
        self.buttons[row][column].config(state=tk.DISABLED)  # Disable the button
        
        if not self.first:  # Check if it's the first tile selected
            self.first = (row, column)  # Store the position of the first tile
        else:
            a, b = self.first
            if self.answer[row][column] == self.answer[a][b]:  # Check if tiles match
                
                # If tiles match, remove them from the grid
                self.answer[row][column] = ''
                self.answer[a][b] = ''
                
                # If no tiles are left, show success message and restart the game after a delay
                if not any(''.join(row) for row in self.answer):
                    duration = time.monotonic() - self.start_time
                    messagebox.showinfo(title='Success!', message='You win! Time: {:.1f}'.format(duration))
                    self.parent.after(750, self.initialize_game)
            else:
                # If tiles don't match, hide them after a delay
                self.parent.after(400, self.hide_tiles, row, column, a, b)
            self.first = None  # Reset the first selected tile
    
    def hide_tiles(self, x1, y1, x2, y2):
        # Hide the selected tiles by resetting their appearance
        self.buttons[x1][y1].config(text='', state=tk.NORMAL)
        self.buttons[x2][y2].config(text='', state=tk.NORMAL)

    def center_window(self):
        # Center the window on the screen
        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()
        
        x = (screen_width - self.parent.winfo_reqwidth()) / 2
        y = (screen_height - self.parent.winfo_reqheight()) / 2 - 100
        
        self.parent.geometry("+%d+%d" % (x, y))

root = tk.Tk()
memory_tile = MemoryTile(root)
root.mainloop()  # Start the GUI main loop

