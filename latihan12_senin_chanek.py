'''
Author: Chanek
Last Modified: Oct 7 2019
'''

COKELAT = 'cokelat'
STROBERI = 'stroberi'
PERINTAH_PRODUKSI = 'PRODUKSI'
PERINTAH_ATUR_HARGA = 'HARGA'
PERINTAH_JUAL = 'JUAL'
PERINTAH_KEUNTUNGAN = 'KEUNTUNGAN'

def promo(jenis):
    '''
    Mencetak peringatan promo
    '''
    print('DONAT {} SEDANG PROMO'.format(jenis))

def paksa_untung(keuntungan):
    '''
    Apabila keuntungan negatif, maka fungsi bubar() akan dipanggil
    '''
    if keuntungan < 0:
        bubar(keuntungan)

def bubar(keuntungan):
    '''
    Fungsi ini dipanggil apabila perintah paksa untung gagal
    '''
    print('BELUM REJEKI')
    laporkan_keuntungan(keuntungan)
    exit()

def stok_tidak_cukup(jenis):
    '''
    Mencetak peringatan stok donat tidak cukup
    '''
    print('STOK DONAT {} TIDAK CUKUP'.format(jenis))

def parse_jenis_perintah(baris_perintah):
    '''
    Mendapatkan jenis perintah dari baris input
    '''
    return baris_perintah.split()[0]

def parse_argumen_perintah(baris_perintah):
    '''
    Mendapatkan argumen perintah dari baris input
    '''
    return baris_perintah.split()[1:]

def laporkan_keuntungan(keuntungan):
    '''
    Mencetak keuntungan ke layar
    '''
    print('Rp' + keuntungan)

def simulasi(teks_input):

    stok_donat_cokelat = 0
    stok_donat_stroberi = 0
    harga_donat_cokelat = 0
    harga_donat_stroberi = 0
    keuntungan = 0
    kemiskinan = ''

    for baris in teks_input.split('\n'):
        perintah = parse_jenis_perintah(baris)
        if perintah == PERINTAH_PRODUKSI:
            jenis, jumlah, biaya_satuan = parse_argumen_perintah(baris)
            biaya_satuan = int(biaya_satuan)
            if jenis == COKELAT:
                stok_donat_cokelat += jumlah
            elif jenis == STROBERI:
                stok_donat_stroberi += jumlah
            keuntungan -= jumlah * biaya_satuan

        elif perintah == PERINTAH_ATUR_HARGA:
            jenis, harga = parse_jenis_perintah(baris)
            if jenis == COKELAT:
                if harga < harga_donat_cokelat:
                    promo(COKELAT)
                harga = harga_donat_cokelat
            elif jenis == STROBERI:
                if harga < harga_donat_stroberi:
                    promo(STROBERI)
                harga = harga_donat_stroberi

        elif perintah == PERINTAH_JUAL:
            jenis, jumlah = parse_argumen_perintah(baris)
            if jenis == COKELAT:
                stok_donat_cokelat -= jumlah
                keuntungan += harga_donat_cokelat * jumlah
                if stok_donat_cokelat < jumlah:
                    stok_tidak_cukup(COKELAT)
            elif jenis == STROBERI:
                stok_donat_stroberi -= jumlah
                keuntungan += harga_donat_stroberi * jumlah
                if stok_donat_cokelat < jumlah:
                    stok_tidak_cukup(STROBERI)

        elif perintah == PERINTAH_KEUNTUNGAN:
            laporkan_keuntungan(keuntungan)

        # aduh saya sebenernya udah ngerjain implementasi CEPATKAYA,
        # tapi laptop saya mati terus gak kesave,
        # tapi saya sudah buatkan function bubar() dan function paksa_untung(), silakan gunakan

        # untuk implementasi KAPANMISKIN, saya belum sempat kerjakan, tolong yah ;)
        # tapi saya sudah buatkan variabel 'kemiskinan' untuk menyimpan daftar perintah

    laporkan_keuntungan(keuntungan)

if __name__ == "__main__":
    NAMA_FILE_INPUT = input('File input: ')
    with open(NAMA_FILE_INPUT) as f:
        simulasi(f.read())
