andi_vs_budi = input('Andi vs Budi: ')
andi_vs_cakra = input('Andi vs Cakra: ')
budi_vs_cakra = input('Budi vs Cakra: ')

# Kita dapat bebas menentukan apa yang dimainkan salah satu anak.
# Karena jika terdapat solusi, kita bisa mencapai solusi itu mau bentuk apapun
# yang dimainkan Andi.
andi = 'batu'

# Tentukan Budi main apa dengan hasil pertandingannya melawan Andi.
if andi_vs_budi == 'Andi menang':
    budi = 'gunting'
elif andi_vs_budi == 'Budi menang':
    budi = 'kertas'
else:
    budi = 'batu'

# Tentukan Cakra main apa dengan hasil pertandingannya melawan Andi.
if andi_vs_cakra == 'Andi menang':
    cakra = 'gunting'
elif andi_vs_cakra == 'Cakra menang':
    cakra = 'kertas'
else:
    cakra = 'batu'

# Periksa apakah konfigurasi yang telah ditentukan konsisten.
# Yang menang harus main batu, lawannya main gunting atau
# yang menang main kertas, lawannya main batu
# atau yang menang main gunting, lawannya main kertas.
# Kalau seri, bentuk yang dimainkan harus sama.
mungkin = True

# Andi vs Budi.
if andi_vs_budi == 'Andi menang':
    mungkin = mungkin and ((andi == 'batu' and budi == 'gunting')
        or (andi == 'kertas' and budi == 'batu')
        or (andi == 'gunting' and budi == 'kertas'))
elif andi_vs_budi == 'Budi menang':
    mungkin = mungkin and ((budi == 'batu' and andi == 'gunting')
        or (budi == 'kertas' and andi == 'batu')
        or (budi == 'gunting' and andi == 'kertas'))
else:
    mungkin = mungkin and (andi == budi)

# Andi vs Cakra.
if andi_vs_cakra == 'Andi menang':
    mungkin = mungkin and ((andi == 'batu' and cakra == 'gunting')
        or (andi == 'kertas' and cakra == 'batu')
        or (andi == 'gunting' and cakra == 'kertas'))
elif andi_vs_cakra == 'Cakra menang':
    mungkin = mungkin and ((cakra == 'batu' and andi == 'gunting')
        or (cakra == 'kertas' and andi == 'batu')
        or (cakra == 'gunting' and andi == 'kertas'))
else:
    mungkin = mungkin and (andi == cakra)

# Budi vs Cakra.
if budi_vs_cakra == 'Budi menang':
    mungkin = mungkin and ((budi == 'batu' and cakra == 'gunting')
        or (budi == 'kertas' and cakra == 'batu')
        or (budi == 'gunting' and cakra == 'kertas'))
elif budi_vs_cakra == 'Cakra menang':
    mungkin = mungkin and ((cakra == 'batu' and budi == 'gunting')
        or (cakra == 'kertas' and budi == 'batu')
        or (cakra == 'gunting' and budi == 'kertas'))
else:
    mungkin = mungkin and (budi == cakra)


if mungkin:
    print('Andi bermain', andi)
    print('Budi bermain', budi)
    print('Cakra bermain', cakra)
else:
    print('Tidak mungkin')