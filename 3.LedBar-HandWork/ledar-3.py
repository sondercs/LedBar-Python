from machine import Pin
import utime

# Array de pinos dos LEDs
led_pins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
led_list = [Pin(pin, Pin.OUT) for pin in led_pins]

def all_leds(led_states):
    for i, led_state in enumerate(led_states):
        led_list[i].value(led_state)
    utime.sleep(0.5)

# Turn the leds ON or OFF 
while True:
    all_leds([1, 1, 1, 0, 0, 1, 1, 1, 1, 1])  
    utime.sleep(0.5)
    all_leds([0, 0, 0, 1, 1, 0, 0, 0, 0, 0])  
    utime.sleep(0.5)
    all_leds([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])  
    utime.sleep(0.5)
    all_leds([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])  
    utime.sleep(0.5)