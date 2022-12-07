import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
states = df["state"]
guessed_state = []


def printing(x, y):
    a = turtle.Turtle()
    a.penup()
    a.hideturtle()
    a.goto(x, y)
    a.write(f"{answer_state}", align="center", font=("Stanley", 12, "normal"))


while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)} / 50 States Correct",
                                    prompt="What's another state's name?").title()
    states = df.state.to_list()

    if answer_state == "Exit":
        missing_states = []
        for s in states:
            if s not in guessed_state:
                missing_states.append(s)
        pd.DataFrame(missing_states).to_csv("States_to_learn.csv")
        break

    if answer_state in states:
        guessed_state.append(answer_state)
        state_data = df[df.state == answer_state]
        printing(int(state_data.x), int(state_data.y))


turtle.mainloop()
screen.exitonclick()
