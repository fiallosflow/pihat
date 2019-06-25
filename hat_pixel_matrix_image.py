#!/usr/bin/env python
#this script will show a matrix of colors on the Pi HAT
from sense_hat import SenseHat
sense = SenseHat ()
r = (255, 0, 0)
b = (0, 0,  255)
w = (255, 255, 255)

pixels = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    w, b, b, w, w, b, b, w, 
    w, w, w, w, w, w, w, w, 
    w, w, w, b, b, w, w, w,
    w, b, b, w, w, b, b, w, 
    b, b, b, b, b, b, b, b, 
    b, b, b, b, b, b, b, b, 
]

sense.set_pixels(pixels)
sense.clear()
