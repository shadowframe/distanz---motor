from machine import Pin, I2C, Timer
from ssd1306 import SSD1306_I2C
import utime
import framebuf
import math


# Es wird I2C 0 verwendet Pin (GP0) und Pin (GP1)
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=40000)
oled = SSD1306_I2C(128,64,i2c)

### SENSOR ###
trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)


# Zeichenfläche wird geleert
oled.fill(0)

# An die Stelle 0, 0 wird "Hello:" geschrieben
oled.text("Hello:",0,0)
oled.show()

# An die Stelle 10, 20 wird zusätzlich "World" geschrieben
oled.text("World",10,20)
oled.show()




def ultra():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   print("The distanceadf from object is ",distance,"cm")
   return distance
   
while True:
   oled.fill(0)   
   ret_val = ultra()
   oled.text("Distance:",0,0)
   oled.text(str(ret_val) + " cm",0,10)
   oled.show()
   utime.sleep(1)

### Geblinke ###

# led = Pin(25, Pin.OUT)
# timer = Timer()
# 
# def blink(timer):
#     led.toggle()
#     print("Hallo")
# 
# timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
