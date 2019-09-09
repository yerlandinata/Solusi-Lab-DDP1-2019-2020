# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:38:48 2019

@author: yerla
"""

import turtle
import math

a = float(input('a: '))
b = float(input('b: '))
t = float(input('t: '))

c_squared = math.pow(t, 2) + math.pow(b-a, 2)

c = math.sqrt(c_squared)

theta_rad = math.asin(t/c)
theta_deg = math.degrees(theta_rad)


turtle.right(180)
turtle.right(theta_deg)
turtle.forward(c)

turtle.left(theta_deg)

turtle.forward(a)

turtle.left(90)

turtle.forward(t)

turtle.left(90)

turtle.forward(b)

turtle.exitonclick()
turtle.mainloop()
