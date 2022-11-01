# MicroPython / Seeed Wio Terminal / SAMD51
# Wio-Terminal-Grove-I2C.py - show how to connect on Grove I2C
# scruss, 2022-10
# -*- coding: utf-8 -*-

from machine import Pin, I2C

# NB: This doesn't do much of anything except list what's
# connected to the left (I²C) Grove connector on the Wio Terminal

i2c = I2C(3, scl=Pin("SCL1"), sda=Pin("SDA1"))
devices = i2c.scan()

if len(devices) == 0:
    print("No I²C devices connected to Grove port.")
else:
    print("Found these I²C devices on the Grove port:")
    for n, id in enumerate(devices):
        print(" device", n, ": ID", id, "(hex:", hex(id) + ")")
