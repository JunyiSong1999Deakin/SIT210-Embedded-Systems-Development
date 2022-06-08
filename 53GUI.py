from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)

led = LED(17)

window=Tk()
window.title("MorseCode") #GUI title
window.geometry("300x300+800+300")#GUI Frame
myFont = tkinter.font.Font(family= 'Helvetica',size=20,weight="bold")#GUI Font

def dot() :
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)


def dash() :
    led.on();
    time.sleep(4)
    led.off()
    time.sleep(1)


def Input_User():
    userInput = Text_Box.get("1.0","end-1c")
    LetterMorseCode(userInput)
    
def LetterMorseCode(userinput):
    for letter in userinput:
        if (letter.lower() == 'a'):
                dot()
                dash()
            
        elif (letter.lower() == 'b'):
                dash()
                dot()
                dot()
                dot()
                
        elif (letter.lower() == 'c'):
                dash()
                dot()
                dash()
                dot()
                
        elif (letter.lower() == 'd'):
                dash()
                dot()
                dot()
                
        elif (letter.lower() == 'e'):
                dot()
                
        elif (letter.lower() == 'f'):
                dot()
                dot()
                dash()
                dot()
                
        elif (letter.lower() == 'g'):
                dash()
                dash()
                dot()
                
        elif (letter.lower() == 'h'):
                dot()
                dot()
                dot()
                dot()
                
        elif (letter.lower() == 'i'):
                dot()
                dot()
                
        elif (letter.lower() == 'j'):
                dot()
                dash()
                dash()
                dash()
            
        elif (letter.lower() == 'k'):
                dash()
                dot()
                dash()
                
        elif (letter.lower() == 'l'):
                dot()
                dash()
                dot()
                dot()
                
        elif (letter.lower() == 'm'):
                dash()
                dash()
                
        elif (letter.lower() == 'n'):
                dash()
                dot()
                
        elif (letter.lower() == 'o'):
                dash()
                dash()
                dash()
                
        elif (letter.lower() == 'p'):
                dot()
                dash()
                dash()
                dot()
                
        elif (letter.lower() == 'q'):
                dash()
                dash()
                dot()
                dash()
                
        elif (letter.lower() == 'r'):
                dot()
                dash()
                dot()
                
        elif (letter.lower() == 's'):
                dot()
                dot()
                dot()
                
        elif (letter.lower() == 't'):
                dash()
                
        elif (letter.lower() == 'u'):
                dot()
                dot()
                dash()
                
        elif (letter.lower() == 'v'):
                dot()
                dot()
                dot()
                dash()
                
        elif (letter.lower() == 'w'):
                dot()
                dash()
                dash()
                
        elif (letter.lower() == 'x'):
                dash()
                dot()
                dot()
                dash()
                
        elif (letter.lower() == 'y'):
                dash()
                dot()
                dash()
                dash()
                
        elif (letter.lower() == 'z'):
                dash()
                dash()
                dot()
                dot()
        
def clear():
    green.off()
    blue.off()
    red.off()
    
    
def exitButton():
    clear()
    window.destroy()
    
Text_Box = Text(window, height = 2, width = 20, bg = "white")
Text_Box.grid(row=0,column=1, padx = 40, pady = 40)

Enter = Button(window, text = 'Execute', font = myFont, command = Input_User, bg = 'white', height = 1, width = 10) 
Enter.grid(row=1,column=1)

exitButton = Button(window, text = 'Exit',font = myFont, command = exitButton, bg = 'white', height = 1, width = 10)
exitButton.grid(row=2, column=1)

window.mainloop()