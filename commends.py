## code for Python 3.4
## please adopt to 2.7 if needed

from tkinter import *

## if you want to use partial function you need the following row
from functools import partial 

## generate a window
newWindow = Tk()

## add window title
newWindow.wm_title("How commands work")

##functions to serve the command part
def function1():
    output["text"] = "1"

def function2():
    output["text"] = "2"

def genFunc(x):
    output["text"] = str(x)
    
##adding the widgets: 1 x Label, 2 x Button
output = Label(newWindow, text="0")

##Option 1:
##input1 = Button(newWindow, command = function1, text = "insert value 1", width = 20)).grid(row=1, column=0)
##input2 = Button(newWindow, command = function2, text = "insert value 2", width = 20)).grid(row=1, column=2)

##Option 2:
##input1 = Button(newWindow, command = lambda: genFunc("1"), text = "insert value 1", width = 20)).grid(row=1, column=0)
##input2 = Button(newWindow, command = lambda: genFunc("2"), text = "insert value 2", width = 20)).grid(row=1, column=2)

##Option 3:
##input1 = Button(newWindow, command = partial(genFunc, 1), text = "insert value 1", width = 20)).grid(row=1, column=0)
##input2 = Button(newWindow, command = partial(genFunc, 2), text = "insert value 2", width = 20)).grid(row=1, column=2)

##Option 4: with text as a variable
##but1 = "1"
##but2 = "2"
##input1 = Button(newWindow, command = partial(genFunc, but1), text = but1, width = 20)).grid(row=1, column=0)
##input2 = Button(newWindow, command = partial(genFunc, but2), text = but2, width = 20)).grid(row=1, column=2)

##Option 5: generating from the list
buttonList = ["1", "2", "3"]
col = 0
for b in buttonList:
    Button(newWindow, text=b, command=partial(genFunc, b), width = 20).grid(row=1, column=col)
    ## shorthand for col = col+1
    col +=1 


##placing the widgets (buttons are placed when they are created. you combine button definition with ".grid()" in one line
output.grid(row=0, column=1)


newWindow.mainloop()
