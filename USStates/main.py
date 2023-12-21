import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

#def get_mouse_click_coor(x, y):
 #   print(x,y)

#turtle.onscreenclick(get_mouse_click_coor)

answer_state = screen.textinput(title="Guess the state", prompt="What's another state name ?")
print(answer_state)
turtle.mainloop()

