import pandas
import turtle

data = pandas.read_csv("states_map.csv")
#conver csv file states to list
all_state_list = data.state.tolist()

list_answer = []

screen =  turtle.Screen()

screen.title("Indian State Quiz Game")
image = "india_states.gif"

screen.bgpic(image)

while len(list_answer) < 50:

    answer_input = screen.textinput(title=f"Guess the state{len(list_answer)}/{50}", prompt="What is the another state?").title()

    if answer_input in all_state_list:
        find_state_data = data[data.state == answer_input]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(find_state_data.x),int(find_state_data.y))

        t.write(answer_input)

        list_answer.append(answer_input)








screen.exitonclick()