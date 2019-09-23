
N = int(input('Banyaknya penanda pada penggaris: '))
x = int(input('Penanda tempat mulai menggaris: '))
y = int(input('Penanda tempat selesai menggaris: '))
print('Gambar Dek Depe:', end=' ')
for i in range(0, N+1):
	if(i==x):
		print('<', sep = '',end='')
	elif(i==y):
		print('>', sep = '', end = '')
	elif(x<i and i<y):
		print('-', sep='', end='')
	else:
		print('.', sep='', end = '')

print()