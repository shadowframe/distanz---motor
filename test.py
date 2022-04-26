from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime
import dcmotor
from hcsr04 import HCSR04

# Es wird I2C 0 verwendet Pin (GP0) und Pin (GP1)
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=40000)
oled = SSD1306_I2C(128, 64, i2c)

# ULTRASCHALL
# distance = sensor.distance_cm()
sensor = HCSR04(trigger_pin=14, echo_pin=15)

# Zeichenfläche wird geleert jhjh
oled.fill(0)


# An die Stelle 0, 0 wird "Hello:" geschrieben
oled.text("Hello:", 0, 0)
oled.show()

# An die Stelle 10, 20 wird zusätzlich "World" geschrieben
oled.text("World", 10, 20)
oled.show()

while True:
    oled.fill(0)
    oled.text("Distance:", 0, 0)
    distance = sensor.distance_cm()
    print('Distance jan:', distance, 'cm')
    oled.text(str(distance) + " cm", 0, 10)
    oled.show()
    if distance < 10:
        dcmotor.forward()
        utime.sleep(2)
        dcmotor.motor_stop()
    utime.sleep(1)
