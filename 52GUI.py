from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

red = LED(17)
blue = LED(27)
green = LED(22)


window=Tk()
window.title("GUI") #GUI title
window.geometry("300x300+800+300")#GUI Frame
ledFont = tkinter.font.Font(family= 'Helvetica',size=20,weight="bold")#GUI Font

def ledToggle():
    clear();
    selectedLedValue =ledValue.get();
    if selectedLedValue ==1:
        red.on()
    if selectedLedValue ==2:
        blue.on()
    if selectedLedValue ==3:
        green.on()
def clear():
    green.off()
    blue.off()
    red.off()
    
    
def exitButton():
    clear()
    window.destroy()
    
 
ledValue =IntVar()
radioRed = Radiobutton(window, text = 'Red LED', font=ledFont,variable = ledValue , value = 1, command = ledToggle)
radioRed.pack(anchor = W)
radioBlue = Radiobutton(window, text = 'Blue LED', font=ledFont,variable = ledValue , value = 2, command = ledToggle)
radioBlue.pack(anchor = W)
radioGreen = Radiobutton(window, text = 'Green LED', font=ledFont,variable = ledValue , value = 3, command = ledToggle)
radioGreen.pack(anchor = W)


exitButton = Button(window, text = 'Exit', command = exitButton)
exitButton.place(x=120,y=120)

window.mainloop()