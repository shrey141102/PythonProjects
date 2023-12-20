import time
import tkinter as tk
import tkinter.font as tkFont
from wonderwords import RandomSentence

X = 90
Y = 20


class Commands:
    def __init__(self):
        self.score = 0
        self.time_taken = 0
        self.t0 = 0
        self.t1 = 0
        self.message = ""

    def clear(self):
        self.t0 = int(time.time() / 10)
        self.score = 0
        entry.delete(0, tk.END)

    def generate_text(self, difficulty=3):
        test_sentences = []

        if difficulty > 3:
            difficulty = 3
        elif difficulty < 1:
            difficulty = 1

        for sentences in range(difficulty * 3):
            s = RandomSentence()
            test_sentences.append(s.sentence())

        return " ".join(test_sentences)

    def calculate_time(self):
        self.t1 = int(time.time())
        self.score = 0
        self.time_taken = self.t1 - self.t0
        self.message = "Done!"
        typed_text_list = typed_text.get().split(" ")
        test_text_list = test_text.split(" ")

        for i in range(len(typed_text_list)):
            if test_text_list[i] and typed_text_list[i]:
                if typed_text_list[i] == test_text_list[i]:
                    self.score += 1

        if self.score == len(test_text_list):
            self.message = "Perfect!"

        score_label = tk.Label(
            root,
            text="SCORE: " + str(self.score),
            anchor=tk.CENTER,
            font="Arial 20 bold",
        )
        score_label.place(x=X, y=Y + 440)

        time_label = tk.Label(
            root,
            text="TIME TAKEN: " + str(self.time_taken) + " s",
            anchor=tk.CENTER,
            font="Arial 20 bold",
        )
        time_label.place(x=X, y=Y + 500)

        message_label = tk.Label(
            root,
            text="MESSAGE: " + str(self.message),
            anchor=tk.CENTER,
            font="Arial 20 bold",
        )
        message_label.place(x=X, y=Y + 560)


commands = Commands()

root = tk.Tk(className="Type Tester")
root.geometry("1250x700")

# App Title
title = tk.Label(root, text="TYPING SPEED TEST", anchor=tk.CENTER, font="Arial 30 bold")
title.place(x=X, y=Y)

# Generate Text
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
text = tk.Label(root, font=fontStyle, wraplength=1100, justify=tk.LEFT)
text.place(x=X, y="90")
test_text = commands.generate_text(1)
text.config(text=test_text)

val = tk.IntVar()
val.set(1)


def set_difficulty():
    test_text = commands.generate_text(val.get())
    text.config(text=test_text)


# Entry Point for Typing
large_font = ("Verdana", 30)
typed_text = tk.StringVar()
entry = tk.Entry(
    root, width=45, bg="#F2BC94", fg="black", font=large_font, textvariable=typed_text
)
entry.place(x=X, y=300)
entry.focus()
t0 = time.time()

# Reset Button
reset = tk.Button(
    root,
    text="RESET",
    bg="black",
    fg="white",
    font="helvetica 20",
    padx=20,
    pady=10,
    command=commands.clear,
)
reset.place(x=X, y=380)

# Calculate Result
result = tk.Button(
    root,
    text="RESULT",
    bg="black",
    fg="white",
    font="helvetica 20",
    padx=20,
    pady=10,
    command=commands.calculate_time,
)
result.place(x=X + 150, y=380)

# Difficulty
difficulty = tk.Button(
    root,
    text="DIFFICULTY",
    bg="black",
    fg="white",
    font="helvetica 20",
    padx=20,
    pady=10,
    command=set_difficulty,
)
difficulty.place(x=X + 320, y=380)
entry = tk.Entry(
    root,
    width=2,
    bg="black",
    fg="white",
    font=large_font,
    textvariable=val,
    borderwidth=10,
    justify="center",
    relief=tk.FLAT,
)
entry.place(x=X + 520, y=380, height=53)

root.mainloop()
