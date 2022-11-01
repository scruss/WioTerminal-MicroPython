# MicroPython / Seeed Wio Terminal / SAMD51
# Wio-Terminal-SDCard.py - mount and use the SD card
# scruss, 2022-10
# -*- coding: utf-8 -*-

from time import sleep_ms
from machine import Pin, SPI
from os import VfsFat, mount, listdir
import sdcard

sd_spi = SPI(6, sck=Pin("SD_SCK"), mosi=Pin("SD_MOSI"),
             miso=Pin("SD_MISO"), baudrate=40000000)
sd = sdcard.SDCard(sd_spi, Pin("SD_CS"))
mount(sd, "/SD")
print(listdir("/SD"))
