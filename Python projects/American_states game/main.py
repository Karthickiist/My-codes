from turtle import Screen
from states import States
import pandas

screen=Screen()
screen.title("Karthick's America States Game")
screen.setup(725,491)
screen.bgpic('blank_states_img.gif')

data=pandas.read_csv('50_states.csv')
all_states=data.state
list=all_states.tolist()
gussed_list=[]
points=0

res=True
while res:
    Input_state = screen.textinput(f"{points}/50 States Correct", 'Enter the state name: ').title()
    if Input_state in list and Input_state not in gussed_list:
        state_data = data[data.state == Input_state]
        x = int(state_data.x)
        y = int(state_data.y)
        gussed_list.append(Input_state)
        list.remove(Input_state)
        state_c=States(Input_state,x,y)
        points+=1
    if points>49 or Input_state=='Exit':
        res=False

missed_states={'Missed states': list}
M_states=pandas.DataFrame(missed_states)
M_states.to_csv("Learner.csv")


screen.exitonclick()