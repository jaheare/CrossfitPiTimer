#Crossfit timer by Jaymes Heare
#For use with Raspberry Pi and Adafruit 16 x 2 LCD plate (or clone)
#http://www.adafruit.com/products/1110


#from Adafruit_CharLCD import Adafruit_CharLCDPlate
# This will err out if you have not set a few things up first.
# Go to https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c to set up the i2c ports properly
# Go to https://learn.adafruit.com/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi/usage for library instalation and basic usage

from time import clock as clock
from time import sleep as sleep
from math import floor as floor

lcd = Adafruit_CharLCDPlate()


lcd.message("Crossfit timer")
lcd.set_color(1,0,0)
sleep(1)
lcd.set_color(0,1,0)
sleep(1)
lcd.set_color(0,0,1)
sleep(1)
lcd.set_color(0,0,0)
lcd.clear()


button = (lcd.LEFT, lcd.UP, lcd.DOWN, lcd.RIGHT, lcd.SELECT)


def delay_countdown():
    # write "GET READY" to second row and blink LED light
    timer_down(10) #can I call this function while blinking the LED?



def stopwatch_up():
    start = clock()
    while 0 != 1:
        now = clock()
        diff = now - start
        tmm = floor(diff / 60)
        tms = floor(diff % 60)
        tmms = floor(((diff % 60) - tms) * 100)
        newTimeList = [tmm,tms,tmms] #will be used to targed just those characters that have changed on the LCD
        # insert call to function writing changes
        print("%02d:%02d:%02d" % (newTimeList[0],newTimeList[1],newTimeList[2])) #testing output
        timeList = newTimeList
        sleep(.01)


def timer_down(start_timer):
    start = clock()
    tmm, tms, tmms, time_over = 0, 0, 0, 0
    newTimeList = [tmm,tms,tmms]
    while time_over == 0:
        now = clock()
        diff = now - start
        display_timer = start_timer - diff
        print("%02d:%02d:%02d" % (newTimeList[0],newTimeList[1],newTimeList[2]))
        tmm = floor(display_timer / 60)
        tms = floor(display_timer % 60)
        tmms = floor(((display_timer % 60) - tms) * 100)
        newTimeList = [tmm,tms,tmms]
        if diff >= start_timer:
            time_over = 1
        sleep(.01)




def tabata_timer_standard():
    for i in range(0,3):
        timer_down(20)
        # statement to address just the status row and change it to "WORK" and change LED color
        timer_down(10)
        # statement to address just the status row and change it to "REST" and change LED color
