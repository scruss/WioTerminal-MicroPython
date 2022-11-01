# MicroPython / Seeed Wio Terminal / SAMD51
# Wio-Terminal-Microphone.py - print values from the microphone
# scruss, 2022-10
# -*- coding: utf-8 -*-

from time import sleep_ms
from machine import ADC

mic = ADC("MIC")

while True:
    print([mic.read_u16()])
    sleep_ms(5)
