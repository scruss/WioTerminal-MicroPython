# MicroPython / Seeed Wio Terminal / SAMD51
# Wio-Terminal-Buzzer.py - play a scale on the buzzer with PWM
# scruss, 2022-10
# -*- coding: utf-8 -*-

from time import sleep_ms
from machine import Pin, PWM

pwm = PWM(Pin("BUZZER", Pin.OUT))  # or Pin(107) or Pin("PD11")
cmaj = [262, 294, 330, 349, 392, 440, 494, 523]  # C Major Scale frequencies

for note in cmaj:
    print(note, "Hz")
    pwm.duty_u16(32767)  # 50% duty
    pwm.freq(note)
    sleep_ms(225)
    pwm.duty_u16(0)  # 0% duty - silent
    sleep_ms(25)
