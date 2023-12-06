# MicroPython / Seeed Wio Terminal / SAMD51
# Wio-Terminal-Screen.py - output something on the ILI9341 screen
# scruss, 2022-10
# -*- coding: utf-8 -*-


from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI


def wheel565(pos):
    # Input a value 0 to 255 to get a colour value.
    # The colours are a transition r - g - b - back to r.
    # modified to return RGB565 value for ili9341 - scruss
    (r, g, b) = (0, 0, 0)
    if (pos < 0) or (pos > 255):
        (r, g, b) = (0, 0, 0)
    if pos < 85:
        (r, g, b) = (int(pos * 3), int(255 - (pos * 3)), 0)
    elif pos < 170:
        pos -= 85
        (r, g, b) = (int(255 - pos * 3), 0, int(pos * 3))
    else:
        pos -= 170
        (r, g, b) = (0, int(pos * 3), int(255 - pos * 3))
    return (r & 0xF8) << 8 | (g & 0xFC) << 3 | b >> 3


# screen can be a little slow to turn on, so use built-in
# LED to signal all is well
led = Pin("LED_BLUE", Pin.OUT)

backlight = Pin("LED_LCD", Pin.OUT)  # backlight is not a PWM pin
spi = SPI(
    7, sck=Pin("LCD_SCK"), mosi=Pin("LCD_MOSI"), miso=Pin("LCD_MISO"), baudrate=4000000
)
display = Display(spi, dc=Pin("LCD_D_C"), cs=Pin("LCD_CS"), rst=Pin("LCD_RESET"))
display.display_on()
display.clear()
led.on()  # shotgun debugging, embedded style
backlight.on()

# use default portrait settings: x = 0..239, y = 0..319
dx = 3
dy = 4
x = 3
y = 4
i = 0

try:
    while True:
        # display.draw_pixel(x, y, wheel565(i))
        display.fill_hrect(x, y, 3, 4, wheel565(i))
        i = (i + 1) % 256
        x = x + dx
        y = y + dy
        if x <= 4:
            dx = -dx
        if x >= 234:
            dx = -dx
        if y <= 5:
            dy = -dy
        if y >= 313:
            dy = -dy
except:
    backlight.off()
    led.off()
    display.display_off()
