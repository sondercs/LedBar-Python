from machine import Pin
import utime

led_list = [0,1,2,3,4,5,6,7,8,9]

for i in range(len(led_list)):
    led_list[i] = Pin(i, Pin.OUT)

while True:
    # On
    for i in range(len(led_list)):
        led_list[i].value(1)
        #utime.sleep(0.5)
    # Await
    utime.sleep(0.5)
    # Off
    for i in range(len(led_list)-1, -1, -1):
        led_list[i].value(0)
    # Await
    utime.sleep(0.5)

'''
{
  "version": 1,
  "author": "Anonymous maker",
  "editor": "wokwi",
  "parts": [
    {
      "type": "wokwi-pi-pico",
      "id": "pico",
      "top": 0,
      "left": 0,
      "attrs": { "env": "micropython-20231227-v1.22.0" }
    },
    {
      "type": "wokwi-led-bar-graph",
      "id": "bargraph1",
      "top": 33.6,
      "left": -72,
      "attrs": { "color": "GYR" }
    }
  ],
  "connections": [
    [ "pico:GND.1", "bargraph1:C1", "black", [ "h0" ] ],
    [ "bargraph1:C1", "bargraph1:C2", "black", [ "v0", "h9.82", "v9.6" ] ],
    [ "bargraph1:C2", "bargraph1:C3", "black", [ "h9.82", "v9.6" ] ],
    [ "bargraph1:C3", "bargraph1:C4", "black", [ "h9.82", "v0", "h0", "v9.6" ] ],
    [ "bargraph1:C4", "bargraph1:C5", "black", [ "h9.82", "v9.6" ] ],
    [ "bargraph1:C5", "bargraph1:C6", "black", [ "h9.82", "v9.59" ] ],
    [ "bargraph1:C6", "bargraph1:C7", "black", [ "h9.82", "v9.59" ] ],
    [ "bargraph1:C7", "bargraph1:C8", "black", [ "h9.82", "v9.59", "h-9.82" ] ],
    [ "bargraph1:C8", "bargraph1:C9", "black", [ "h9.82", "v9.59" ] ],
    [ "pico:GP0", "bargraph1:A1", "green", [ "h-82.8", "v25.65" ] ],
    [ "pico:GP1", "bargraph1:A2", "green", [ "h-82.8", "v25.65" ] ],
    [ "pico:GP2", "bargraph1:A3", "green", [ "h-15.6", "v-41.55", "h-67.2", "v57.6" ] ],
    [ "pico:GP3", "bargraph1:A4", "green", [ "h-15.6", "v-60.75", "h-67.2", "v76.8" ] ],
    [ "pico:GP4", "bargraph1:A5", "green", [ "h-15.6", "v-79.95", "h-67.2", "v96" ] ],
    [ "pico:GP5", "bargraph1:A6", "green", [ "h-15.6", "v-99.15", "h-67.2", "v115.2" ] ],
    [ "pico:GP6", "bargraph1:A7", "green", [ "h-15.6", "v-127.95", "h-67.2", "v134.4" ] ],
    [ "pico:GP7", "bargraph1:A8", "green", [ "h-15.6", "v-147.15", "h-67.2", "v153.6" ] ],
    [ "pico:GP8", "bargraph1:A9", "green", [ "h-15.6", "v-166.35", "h-67.2", "v172.8" ] ],
    [ "pico:GP9", "bargraph1:A10", "green", [ "h-15.6", "v-185.55", "h-67.2", "v192" ] ],
    [ "bargraph1:C9", "bargraph1:C10", "black", [ "h9.82", "v9.59" ] ]
  ],
  "dependencies": {}
}
    '''


