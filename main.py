import  turtle
import pandas

screen=turtle.Screen()

image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.title("U.S state Game")

timmy=turtle.Turtle()
# timmy.goto(100,100)
timmy.hideturtle()

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data=pandas.read_csv("50_states.csv")
state_list=data.state.tolist()
# print(state_list)


# print(state_name)
state_guess=[]
x_cor=0
y_cor=0
count=0
while count<50:
    state_name = screen.textinput(title=f"{count}/50 States Correct", prompt="Enter the state name..").title()
    if state_name=="Exit":
        break;
    if (state_name in state_list):
        if state_name in state_guess:
            pass
        else:
            state_guess.append(state_name)
            x_cor=int(data[data.state==state_name].x)
            y_cor=int(data[data.state==state_name].y)
            timmy.penup()
            timmy.goto(x_cor,y_cor)
            timmy.pendown()
            timmy.write(f"{state_name}",align="center", font=("Arial", 8, "normal"))
            count+=1

not_guess={
    "name":[]
}
for i in state_list:
    if i in state_guess:
        pass
    else:
        not_guess["name"].append(i)

newww=pandas.DataFrame(not_guess)
newww.to_csv("state_not_guessed.csv")
# print(not_guess)