#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat ()
import time 
import random
r= random.randint (0,7)
y= random.randint (0,7)
p= random.randint (0,255)
sense.set_pixel(r, y,  (p, p, p))
time.sleep(1)
sense.clear()
