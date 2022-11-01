# MicroPython / Seeed Wio Terminal / SAMD51
# Wio-Terminal-LED.py - blink the internal blue LED
# scruss, 2022-10
# -*- coding: utf-8 -*-

from machine import Pin
from time import sleep_ms

led = Pin("LED_BLUE", Pin.OUT)  # or Pin(15) or Pin("PA15")

try:
    while True:
        led.value(not led.value())
        sleep_ms(1200)
except:
    led.value(0)  # turn it off if user quits
    exit()
