import Adafruit_CharLCD as LCD
lcd = LCD.Adafruit_CharLCDPlate()
import time
import subprocess

displaytext = "cobalt"

IP= subprocess.check_output('hostname','-I')

lcd.clear
lcd.message(displaytext)

while (True):
    if lcd.is_pressed(LCD.SELECT):
        lcd.message("  hello world")
        lcd.clear()


else:
    lcd.message(IP)
