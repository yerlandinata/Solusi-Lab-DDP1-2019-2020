# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 14:58:38 2019

@author: yerla
"""

import turtle

warna_kesukaan = input('Apa warna kesukaan mu? ')

if warna_kesukaan == 'merah':
    turtle.color('red')
elif warna_kesukaan == 'hijau':
    turtle.color('green')
elif warna_kesukaan == 'kuning':
    turtle.color('yellow')
    
if warna_kesukaan != 'merah' and warna_kesukaan != 'hijau' and warna_kesukaan != 'kuning':
    turtle.forward(100)

    turtle.right(90)
    turtle.forward(100)
    
    turtle.right(90)
    turtle.forward(100)
    
    turtle.right(90)
    turtle.forward(100)
else:
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()


turtle.hideturtle()

turtle.exitonclick()
turtle.mainloop()
