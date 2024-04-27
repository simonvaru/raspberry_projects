from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

### HARDWARE DEFINITIONS ###
# LED pin definitions

led5 = LED(18)
led6 = LED(15)
led7 = LED(14)
# Arrange LEDs into a list
leds = [led7,led6,led5]

### GUI DEFINITIONS ###
root=Tk()
root.geometry("350x65")
root.title("LED Controller v.LITE")
myFont=tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")
ledCode = StringVar()


### Event Functions ###
def ledShow():
    ledCode = code.get()
    print("LED code: ", ledCode) #Debug

    i=0 #loop-counter
    # For each character in the ledCode string, check if = 1 and if so,
    # turn on the corresponding LED
    for j in ledCode:
        if j == "1":
            leds[i].on()
        else:
            leds[i].off()
        i+=1

def close(): # Cleanly close the GUI and cleanup the GPIO
    RPi.GPIO.cleanup()
    root.destroy()


### WIDGETS ###

ledButton = Button(root, text='Load LED code', font=myFont, command=ledShow, bg='bisque2', height=1, width=25)
ledButton.grid(row=0,column=1)

code = Entry(root, font=myFont, width=5)
code.grid(row=0,column=0)

exitButton = Button(root, text='Exit', font=myFont, command=close, bg='red', height=1, width=25)
exitButton.grid(row=3,column=1, sticky=E)

root.protocol("WM_DELETE_WINDOW", close) # cleanup GPIO when user closes window

root.mainloop() # Loops forever