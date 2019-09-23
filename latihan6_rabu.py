nilai = int(input())

# Menentukan kategori.
kategori = 'E'
if nilai > 85:
    kategori = 'A'
elif nilai > 75:
    kategori = 'B'
elif nilai > 65:
    kategori = 'C'
elif nilai > 49:
    kategori = 'D'

print('Kucing berkategori ' + kategori, end=', ')
# Hanya membeli kucing dengan kategori C ke atas.
if kategori < 'D':
    print('beli!')
else:
    print('jangan dibeli!')