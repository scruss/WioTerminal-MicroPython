# MicroPython / Seeed Wio Terminal / SAMD51
# Wio-Terminal-Buttons.py - test the buttons
# scruss, 2022-10
# -*- coding: utf-8 -*-

# using Signal because button sense is inverted: 1 = off, 0 = on
from machine import Pin, Signal
from time import sleep_ms

pin_names = [
    "BUTTON_3",  # Pin(92)  or Pin(PC28) - top left
    "BUTTON_2",  # Pin(91)  or Pin(PC27) - top middle
    "BUTTON_1",  # Pin(90)  or Pin(PC26) - top right
    "SWITCH_B",  # Pin(108) or Pin(PD12) - joystick left
    "SWITCH_Y",  # Pin(105) or Pin(PD09) - joystick right
    "SWITCH_U",  # Pin(116) or Pin(PD20) - joystick up
    "SWITCH_X",  # Pin(104) or Pin(PD08) - joystick down
    "SWITCH_Z",  # Pin(106) or Pin(PD10) - joystick button
]

pins = [None] * len(pin_names)
for i, name in enumerate(pin_names):
    pins[i] = Signal(Pin(name, Pin.IN), invert=True)

while True:
    for i in range(len(pin_names)):
        print(pins[i].value(), end="")
    print()
    sleep_ms(100)
