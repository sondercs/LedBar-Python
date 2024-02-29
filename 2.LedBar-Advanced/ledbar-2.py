from machine import Pin
import utime

# Array leds
led_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Initialize all LEDs and outputs
for i in range(len(led_list)):
    led_list[i] = Pin(i, Pin.OUT)

# Function to turn all LEDs ON
def turn_on_leds(led_state=1):
    for i in range(len(led_list)):
        led_list[i].value(led_state)
        utime.sleep(0.5)

# Function to turn all LEDs OFF
def turn_off_leds(led_state=0):
    for i in range(len(led_list)-1, -1, -1):
        led_list[i].value(led_state)
        utime.sleep(0.5)

# Blink the LEDs on and off
while True:
    turn_on_leds(1)
    utime.sleep(0.5)
    turn_off_leds(0)
    utime.sleep(0.5)
