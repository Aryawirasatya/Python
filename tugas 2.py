MIN_QTY = 30
harga_barang = 30000

hasil = MIN_QTY * harga_barang
print (hasil)

print('=' * 43)
print('AKU ANAK PPLG YANG KUAT DAN SEMANGAT 😎👍')
print('-' * 43)

nama_barang = 'kertas'
jumlah_barang= 20
harga = 100000
ketersediaan= True

print('\tNAMA BARANG:',nama_barang)
print('\tJUMLAH BARANG:',jumlah_barang)
print('\tHARGA:',harga)
print("\tKETERSEDIAAN:",ketersediaan)

angka1 = 87.77
angka2 = 66.50
angka3 = 97.5

jumlah = angka1 + angka2 + angka3
rata_rata = jumlah/3

print('\tangka 1:',angka1)
print('\tangka 2:',angka2)
print('\tangka 3:',angka3)
print ('\tjumlah:',jumlah)
print ('\trata rata',rata_rata)

kelompok = input('\tmasukan nama kelompok:')
asal= input('\tmasukan asal kelompok:')
jumlah_tim = int(input('\tmasukan jumlah anggota tim:'))
usia = int(input('\tmasukan usia:'))
print('===========================================')
print('\tnama kelompoknya adalah:',kelompok)
print('\tasal kelompok dari:',asal)
print('\tjumlah kelompok adalah',jumlah_tim)
print('\tusia:' ,usia)


barang1 = int(input('\tmasukan jumkah barang pertama:'))
barang2 = int(input('\tmasukan jumlah barang kedua:'))
barang3 = int(input('\tmasukan jumlah barang ketiga:'))
barang4 = int(input('\tmasukan jumlah barang keempat:'))

total = barang1 + barang2 + barang3 + barang4

print('\ttotal jumlah semua barang adalah:',total)

harga_barang = float(input('\tmasukan harga barang:'))

if harga_barang >= 100000:
    print('\tselamat anda mendapatkan diskon 5%')


elif harga_barang < 100000:
     print('\tmaaf pembelian anda di bawah ketentuan diskon ')

else:
    print('\tmaaf input anda tidak valid: ')

diskon = harga_barang / 5
print('\ttotal setelah diskon adalah:')


harga_barang = float(input('\tMasukan harga barang: '))

if  harga_barang >= 100000:
    diskon = harga_barang * 0.05
    harga_setelah_diskon = harga_barang - diskon
    print('\tSelamat, Anda mendapatkan diskon 5%')
    print('\tTotal setelah diskon adalah:''Rp', harga_setelah_diskon,)

elif harga_barang < 100000 and harga_barang > 0:
    print('\tMaaf, pembelian Anda di bawah ketentuan diskon')

else:
    print('\tMaaf, input Anda tidak valid')











