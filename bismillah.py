# # # no 1
# # print('Hello world')    
# # print('=' *25)
# # print('Hello algoritma','-'*25)

# # # no 2
# # print('='*20)
# # print('PROGRAM PERSEGI')
# # print('='*20)

# # sisi = float(input('masukan sisi:'))

# # luas = sisi * sisi
# # keliling = sisi+sisi+sisi+sisi

# # print('luas:',luas,'cm2')
# # print('keliling:',keliling,'cm')

# # print('='*20)
# # print('PROGRAM SEGITIGA')
# # print('='*20)

# # tinggi = float(input('masukan Tinggi:'))
# # alas = float(input('masukan Alas:'))
# # sisi = float(input('masukan sisi:'))
# # luas = 0.5 * alas * tinggi
# # keliling = sisi + sisi + sisi

# # print ('luas:',luas,'cm2')
# # print ('keliling:',keliling,'cm')

# # print('='*20)
# # print('PROGRAM LINGKARAN')
# # print('='*20)

# # PHI = 3.14

# # r = float(input('masukan jari-jari:'))

# # luas = PHI * r**2
# # keliling = 2 * PHI * r

# # print('luas:',luas,'cm2')
# # print('keliling:',keliling,'cm')

# # print('='*30)
# # print('PROGRAM KONVERSI SUHU')
# # print('='*30)

# # celcius = float(input('masukan suhu(dalam celcius):'))

# # fahrenheit = ((9/5) * celcius) + 32
# # print('suhu dalam fahrenheit:',fahrenheit,)

# # reamur = (4/5) * celcius
# # print('suhu dalam reamur:',reamur,)

# # print('='*30)
# # print('PROGRAM KELULUSAN')
# # print('='*30)

# # nilai = float(input('masukan nilai:'))

# # if nilai >= 75:
# #     print('lulus')

# # elif nilai <= 75:
# #     print('tidak lulus')

# # print('Hello friends!')

# # print(4122007)
# # print('human')

# # x = 100
# # teks = "ngoding"

# # print(x)
# # print(teks)

# # firstinteger = 30
# # secondinteger = '40'
# # secondinteger =int(secondinteger)

# # hasil = firstinteger + secondinteger

# # print('hasilnya adalah',hasil)

# # firstDecimal = 4.54
# # secondDecimal = "3.74"

# # secondDecimal = float(secondDecimal)

# # hasil = firstDecimal +  secondDecimal

# # print('hasilnya adalah',hasil)

# # firstring = 'hidup'
# # secondstring = 'adalah perjuangan'

# # hasil = firstring + " " + secondstring
# # print(hasil)

# # nama_barang = 'kertas'
# # jumlah_barang = 20
# # harga_barang = 1000000
# # ketersediaan = True

# # print('Nama barang:',nama_barang)
# # print('jumlah barang:',jumlah_barang)
# # print('harga barang:',harga_barang)
# # print('ketersediaan:',ketersediaan)

# # angka1 = 87.77
# # angka2 = 66.50
# # angka3 = 97.5

# # rerata_a1_a2 = (angka1 + angka2) / 2
# # hasil_semua = angka1 + angka2 + angka3
# # rata_rata_semua = (angka1 + angka2 + angka3) / 3


# # print('rata-rata angka 1 dan 2 adalah:',rerata_a1_a2)
# # print('hasil penjumlahan:',hasil_semua)
# # print('rata-rata semua angka:',rata_rata_semua)


# # kelompok = input('asal kelompok:')
# # asal_daerah = input('asal daerah:')
# # jumlah_team = int(input('jumlah team:'))

# # print()

# # print ('kelompok:',kelompok)
# # print ('asal daerah:',asal_daerah)
# # print ('jumlah team:',jumlah_team)


# # barang1 = int(input('barang 1 : '))
# # barang2 = int(input('barang 2 : '))
# # barang3 = int(input('barang 3 : '))
# # barang4 = int(input('barang 4 : '))

# # total = barang1 + barang2 + barang3 + barang4

# # print('totalnya adalah',total,'buah')





# while True:
#     harga_barang = float(input('masukan harga barang yang anda beli : Rp'))

#     if harga_barang >= 100000:
#        diskon = harga_barang * 0.05
#        harga_setelah_diskon = harga_barang - diskon
#        print('selamat anda telah mendapatkan diskon 5%')
#        print(f'harga barang anda setelah mendapat diskon :Rp{harga_setelah_diskon} ')
    
#     elif harga_barang <= 100000:
#         print('maaf, anda tidak memenuhi syarat diskon')

#     else:
#         print('input anda tidak valid')    

#     ulang = input('apakah anda ingin mengulang program? {ya/tidak}:').lower()

#     if ulang == 'ya':
#         continue
#     if ulang == 'tidak':
#         print('='*30)
#         print('terimakasih telah berbelanja di toko kami😁👍')
#         print('='*30)


bil1 = int(input('masukan angka pertama : '))
bil2 = int(input('masukan angka kedua : '))
bil3 = int(input('masukan angka ketiga :'))
print('-'*45)

if bil1 > bil2 and bil1 > bil3 :
    print(f'yang terbesar adalah {bil1}')
elif bil2 > bil3 and bil2 > bil1:
    print(f'yang terbesar adalah {bil2}')
elif bil3 > bil1 and bil3 > bil2:
    print(f'yang terbesar adalah {bil3}')
print('-'*45)
if bil1 < bil2 and bil1 < bil3:
    print(f'yang terkecil adalah {bil1}')
elif bil2 < bil3 and bil2 < bil1:
    print(f'yang terkecil adalah {bil2}')
elif bil3< bil1 and bil3 < bil2 :
    print(f'yang terkecil adalah {bil3}')

print('-'*45)












