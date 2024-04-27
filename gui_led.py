## Toggle an LED when the GUI button is pressed ##

from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

### HARDWARE DEFINITIONS ###
led=LED(14)

### GUI DEFINITIONS ###
win = Tk()#root=Tk()
win.title("LED TOGGLER")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")


### Event Functions ###
def ledToggle():
    if led.is_lit:
        led.off()
        ledButton["text"]="Turn LED ON" # Change only the button text property
        led_1["bg"]='red'
    else:
        led.on()
        ledButton["text"]="Turn LED OFF"
        led_1["bg"]='green'

def close():
    RPi.GPIO.cleanup()
    win.destroy()



### WIDGETS ###

# Button, triggers the connected command when it is pressed
ledButton = Button(win, text='Turn LED ON', font=myFont, command=ledToggle, bg='white', height=1, width=24)
ledButton.grid(row=0,column=1)

led_1=Canvas(win, height=10, width=10, bg='red')
led_1.grid(row=0,column=2)

exitButton = Button(win, text='Exit', font=myFont, command=close, bg='white', height=1, width=6)
exitButton.grid(row=2, column=1)

win.protocol("WM_DELETE_WINDOW", close) # cleanup GPIO when user closes window

win.mainloop() # Loops foreverchromebook




