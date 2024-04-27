## A demonstration of some Tkinter widgets ##

from tkinter import *
import tkinter.font

### GUI DEFINITIONS ###
root = Tk()
root.title("GUI Home Menu")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

leftFrame = Frame(root)
leftFrame.pack(side = LEFT)
rightFrame = Frame(root)
rightFrame.pack(side = RIGHT)
midFrame = Frame(root)
midFrame.pack(side = RIGHT)

### Variable Definitions for widgets ###
checkVal1 = IntVar()
checkVal2 = IntVar()
sliderval = DoubleVar()
rad = "Str()"

### Event Functions ###
def buttonPress():
    print('Home Temperature value is {}' .format(sliderval.get()))

def checkToggle():
    print('\nCheckbox #1  #2\n          {}   {}' .format(checkVal1.get(), checkVal2.get()))

def checkRadio():
    select = "Alarm arm" 
    label.config(text = select)

def close():
    win.destroy()   # Close GUI

### WIDGETS ###

# Button, triggers the connected command when it is pressed
myButton = Button(midFrame, text='SET (°C)', font=myFont, command=buttonPress, bg='bisque2', height=1)
myButton.pack(side = BOTTOM)

# Two checkboxes, update attached variables and call command when toggled
check1 = Checkbutton(leftFrame, text='Lights   ', variable=checkVal1, command=checkToggle)
check1.pack()
check2 = Checkbutton(leftFrame, text='A/C', variable=checkVal2, command=checkToggle)
check2.pack()

# Radio Buttons - good for mutually exclusive options
label = Label(leftFrame)
label.pack()
label.config(text="Alarm disarm")
R1 = Radiobutton(leftFrame, text="Home Alone Alarm",variable=rad, value=1, command = checkRadio)
R1.pack()
R2 = Radiobutton(leftFrame, text="Perimetral Alarm",variable=rad, value=2, command = checkRadio)
R2.pack()

# Slider bar - Good for more continuous parameter adjustment
slider = Scale(midFrame, variable = sliderval, from_=40, to=15)
slider.pack()

# Spinbox - select from a range of predetermined values
numOption = Spinbox(rightFrame, text="Humidity", from_=10, to = 50, width=5)
numOption.pack(side = TOP )


# Exit Button - closed the GUI
exitButton = Button(rightFrame, text='Exit', font=myFont, command=close, bg='red', height=1, width=6)
exitButton.pack(side = BOTTOM )

root.mainloop() # Loops forever