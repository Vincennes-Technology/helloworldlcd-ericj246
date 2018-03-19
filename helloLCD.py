#!/usr/bin/python
#show "hello world on the lcd screen"
# cobalt

import Adafruit_CharLCD as LCD





displayText = "hello world"

while (True):
    if lcd.is_pressed(LCD.SELECT):
        lcd.message("hello world") 

lcd.clear()
lcd.message(displayText)
