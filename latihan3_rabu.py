import turtle
import math

# Gambar sisi alas.
turtle.forward(100)

# Belok kiri, gambar sisi tinggi.
turtle.left(90)
turtle.forward(100)

# belok kiri, gambar sisi miring.
turtle.left(180 - 45)
turtle.forward(100 * math.sqrt(2))

turtle.exitonclick()
turtle.mainloop()