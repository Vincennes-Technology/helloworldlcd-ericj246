#!/usr/bin/python
#show IP adress on LCD plate at start up
#cobalt


import Adafruit_CharLCD as LCD
import time
import subprocess

lcd = LCD.Adafruit_CharLCDPlate()

Name = subprocess.check_output(['hostname']).strip()
displaytext = Name

IPaddr = subprocess.check_output(['hostname', ' -I']).split()
refresh = True

while (True):
    if lcd.is_pressed(LCD.SELECT):
        lcd.clear()
        lcd.message(displaytext + "\n")
        lcd.message("  Hello world\n")
        refresh = True


    else:
        if refresh:
            lcd.clear()
            lcd.message(displaytext + "\n")
            lcd.message(IPaddr[0])
            refresh = False
    time.sleep(0.25)