import turtle
import pandas
screen=turtle.Screen()
score=0
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


#answer_state=screen.textinput(title="Guess the State",prompt="what's another state")
#print(answer_state.title(#))

#ata=pandas.read_csv("50_states.csv")
data=pandas.read_csv("50_states.csv")
guessed_state=[]
game_on=True
while len(guessed_state)<50:

    answer_state = screen.textinput( title=f"{score}/50 states correct", prompt=" what's another state").title()
    print(answer_state)
    if answer_state=="Exit":
        missing_state=[]
        for state in data.state:
            if state not in guessed_state:
                missing_state.append(state)

        print(missing_state)
        file=pandas.DataFrame(missing_state)
        file.to_csv("missing_state.csv")




        break




    for answer in data.state:

            if answer_state==answer:
                t1=turtle.Turtle()
                t1.hideturtle()
                t1.penup()
                state_data=data[data.state==answer_state]
                t1.goto(state_data.x.item(),state_data.y.item())
                t1.write(answer_state)
                guessed_state.append(answer)
                score+=1
                print("yes")













screen.exitonclick()