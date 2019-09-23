import turtle

rasa = input('Masukan rasa donat: ')

# Menentukan warna donat berdasarkan rasa.
if rasa == 'Cokelat':
    turtle.color('brown')
elif rasa == 'Stroberi':
    turtle.color('red')

# Menggambar lingkaran dengan isi warna yang telah ditentukan.
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

# Memindahkan posisi turtle untuk menggambar lingkaran kecil:
# Belok kiri, maju sebanyak setengah jari-jari lingkaran
# besar. Putar lagi arah turtle ke kanan.
turtle.left(90)
turtle.forward(50)
turtle.right(90)

# Menggambar lingkaran kecil berwarna putih
turtle.color('white')
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

# Sembunyikan turtle.
turtle.ht()

turtle.exitonclick()
turtle.mainloop()