import RPi.GPIO as GPIO
import time
import os

#adjust for where your switch is connected
#buttonPin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)
GPIO.setup(15,GPIO.OUT)
#input = GPIO.input(17)

#while True:
  #assuming the script to call is long enough we can ignore bouncing
 # if (GPIO.input(17)):
    #this is the script that will be called (as root)
    #os.system("sudo python /home/pi/led_on.py")
prev_input = 0
while True:
  #take a reading
  input = GPIO.input(11)
  #if the last reading was low and this one high, print
  if ((not prev_input) and input):
    print("START")	
    #once the button is pressed, the script will run and there will be a single beep sound.
    os.system('python /home/pi/tah_final.py')
    GPIO.output(15,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(15,GPIO.LOW)		 
  #update previous input
  prev_input = input
  #slight pause to debounce
  time.sleep(0.05)
