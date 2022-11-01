# MicroPython / Seeed Wio Terminal / SAMD51
# Wio-Terminal-IR_LED.py - blink the internal IR LED
# scruss, 2022-10
# -*- coding: utf-8 -*-

# Hey! This is a completely futile exercise, unless you're able
# to see into the IR spectrum. But we're here to show you the pin
# specification to use. For actual useful libraries to do stuff with
# IR, take a look on https://awesome-micropython.com/#ir

# So this is a boring blink, 'cos we're keeping it short here.
# You might be able to see the LED (faintly) with your phone camera

from machine import Pin, PWM
from time import sleep_ms

ir = PWM(Pin("PB31"))  # "IR_CTL" not currently defined

try:
    while True:
        ir.duty_u16(32767)  # 50% duty
        ir.freq(38000)  # fast flicker
        sleep_ms(1200)
        ir.duty_u16(0)  # off
        sleep_ms(1200)
except:
    ir.duty_u16(0)  # turn it off if user quits
    exit()
