
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

trig = 18
echo = 17
buzz = 16

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(buzz, GPIO.OUT)


def distance_calculator():
  GPIO.output(trig, 1) 
  time.sleep(0.00001) 
  GPIO.output(trig, 0) 
 
  time_b = time.time()
  time_e = time.time()
  
  while GPIO.input(echo) == 0:
    time_b = time.time()
 
  while GPIO.input(echo) == 1:
    time_e = time.time()
  
  val_time = time_e - time_b
  val_distance = val_time * 34300 / 2

  print("Distance between sensor and object:", val_distance, " cm")
  
  return val_distance

def frenqucy_buzz():
  
  distance = distance_calculator()
  
  if distance > 80:
    return -1
  elif distance <= 80 and distance >=60:
    return 1
  elif distance < 60 and distance >= 30:
    return 0.6
  elif distance < 30 and distance >= 10:
    return 0.3
  else:
    return 0

def Execute():
  try:
    while True:
      freq = frenqucy_buzz()
      
      if freq == -1:
        GPIO.output(buzz, False)
        time.sleep(0.2)
      
      elif freq == 0:
        GPIO.output(buzz, True)
        time.sleep(0.2)
      else:
        GPIO.output(buzz, True)
        time.sleep(0.2) 
        GPIO.output(buzz, False)
        time.sleep(freq) 
  
  except KeyboardInterrupt:
    GPIO.output(buzz, False)
    GPIO.cleanup()

if __name__ == "__main__":
    Execute()
