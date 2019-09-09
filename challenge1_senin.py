import turtle
import math

r1 = float(input())
r2 = float(input())
d = float(input())
 
# mulai gambar r2
turtle.circle(r2)
turtle.forward(d)
 
# math stuff
sudut = math.atan(d/(r1 - r2))
sudut = 360 - 2*math.degrees(sudut)
 
# gambar lingkaran r1
turtle.circle(r1)
 
# gerak ke posisi singgung
turtle.circle(r1, sudut)
 
# buat garis singgung
turtle.forward(d)
turtle.exitonclick()
