import RPi.GPIO as GPIO
import time
import requests
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


Button_pin = 4
GPIO.setup(Button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

milk_amount = 0

def outputFunction(null):
        print("Signal detected")
        requests.post('https://maker.ifttt.com/trigger/Added/with/key/pFJDSyx0RpTYzJ2KI8D2Cp9rdi3RxVf8XJaXKkFNs2r')
 
GPIO.add_event_detect(Button_pin, GPIO.FALLING, callback=outputFunction, bouncetime=100)
# main program loop
try:
    while True:
        time.sleep(5)
  
# clean up after the program is finished
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

