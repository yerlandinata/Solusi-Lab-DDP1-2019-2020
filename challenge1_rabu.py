import turtle

# Gambar lingkaran kuning.
turtle.color('yellow')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

# Pindahkan turtle ke posisi mata kiri.
turtle.goto(-50, 120)

# Gambar mata kiri.
turtle.color('black')
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

# Ganti warna turtle menjadi kuning agar perpindahan
# turtle tidak meninggalkan bekas.
turtle.color('yellow')

# Pindahkan turtle ke posisi mata kanan.
turtle.goto(50, 120)

# Gambar mata kanan.
turtle.color('black')
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

# Ganti warna turtle menjadi kuning agar perpindahan
# turtle tidak meninggalkan bekas.
turtle.color('yellow')

# Pindahkan turtle ke posisi senyum.
turtle.goto(-70, 100)

# Ubah orientasi turtle agar mulai menggambar ke arah bawah.
turtle.setheading(-90)

# Memindahkan turtle 30 / 360 lingkaran.
turtle.circle(70, 30)

# Menggambar senyum dengan 120 / 360 lingkaran.
turtle.color('black')
turtle.circle(70, 120)

# Sembunyikan turtle.
turtle.ht()

turtle.exitonclick()
turtle.mainloop()