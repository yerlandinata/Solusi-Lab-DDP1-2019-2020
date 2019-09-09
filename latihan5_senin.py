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

c = math.sqrt(math.pow(t, 2) + math.pow(b-a, 2))
alpha_rad = math.asin(t/c)
alpha_deg = math.degrees(alpha_rad)

turtle.right(180)
turtle.right(alpha_deg)
turtle.forward(c)

turtle.left(alpha_deg)

turtle.forward(a)

turtle.left(90)

turtle.forward(t)

turtle.left(90)

turtle.forward(b)

turtle.exitonclick()
turtle.mainloop()
