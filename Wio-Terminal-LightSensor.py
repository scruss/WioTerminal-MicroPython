# MicroPython / Seeed Wio Terminal / SAMD51
# Wio-Terminal-LightSensor.py - print values from the light sensor
# scruss, 2022-10
# -*- coding: utf-8 -*-

from time import sleep_ms
from machine import ADC

# PD15-22C/TR8 photodiode
light_sensor = ADC("PD01")

while True:
    print([light_sensor.read_u16()])
    sleep_ms(50)
