#!/usr/bin/python
#show "hello world on the lcd screen"
# cobalt

import Adafruit_CharLCD as LCD


lcd = LCD.Adafruit_CharLCDPlate()

displayText = "hello world"

lcd.clear()
lcd.message(displayText)
