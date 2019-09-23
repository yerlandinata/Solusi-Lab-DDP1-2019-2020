andi_vs_budi = input('Andi vs Budi: ')
andi_vs_cakra = input('Andi vs Cakra: ')
budi_vs_cakra = input('Budi vs Cakra: ')

# Inisialisasi bentuk yang dimainkan setiap pemain.
andi = 'batu'
budi = 'batu'
cakra = 'batu'

# Periksa setiap pertandingan, pemain yang kalah berarti bermain gunting.

# Andi vs Budi
if andi_vs_budi == 'Andi menang':
    budi = 'gunting'
elif andi_vs_budi == 'Budi menang':
    andi = 'gunting'

# Andi vs Cakra
if andi_vs_cakra == 'Andi menang':
    cakra = 'gunting'
elif andi_vs_cakra == 'Cakra menang':
    andi = 'gunting'

# Budi vs Cakra
if budi_vs_cakra == 'Budi menang':
    cakra = 'gunting'
elif budi_vs_cakra == 'Cakra menang':
    budi = 'gunting'


# Periksa apakah konfigurasi yang telah ditentukan konsisten.
# Yang menang harus main batu, yang kalah main gunting.
# Kalau seri, bentuk yang dimainkan harus sama.
mungkin = True

# Andi vs Budi.
if andi_vs_budi == 'Andi menang':
    mungkin = mungkin and (andi == 'batu' and budi == 'gunting')
elif andi_vs_budi == 'Budi menang':
    mungkin = mungkin and (andi == 'gunting' and budi == 'batu')
else:
    mungkin = mungkin and (andi == budi)

# Andi vs Cakra.
if andi_vs_cakra == 'Andi menang':
    mungkin = mungkin and (andi == 'batu' and cakra == 'gunting')
elif andi_vs_cakra == 'Cakra menang':
    mungkin = mungkin and (andi == 'gunting' and cakra == 'batu')
else:
    mungkin = mungkin and (andi == cakra)

# Budi vs Cakra.
if budi_vs_cakra == 'Budi menang':
    mungkin = mungkin and (budi == 'batu' and cakra == 'gunting')
elif budi_vs_cakra == 'Cakra menang':
    mungkin = mungkin and (budi == 'gunting' and cakra == 'batu')
else:
    mungkin = mungkin and (budi == cakra)


if mungkin:
    print('Andi bermain', andi)
    print('Budi bermain', budi)
    print('Cakra bermain', cakra)
else:
    print('Tidak mungkin')