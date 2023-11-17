print('=' * 25)
print('\nKONVERSI TEMPERATUR SUHU\n')

celcius = float(input('masukan suhu dalam celcius :'))

print('suhunya adalah',celcius,'celcius')

reamur = (4/5) * celcius
print('suhunya adalah',reamur,"reamur")

fahrenheit = ((9/5) * celcius) + 32
print('hasilnya adalah',fahrenheit,'fahrenheit')

kelvin = celcius + 273
print ('hasilnya adalah',kelvin,'kelvin')
print("-" * 25)



fahrenheit = int(input('masukan suhu dari fahrenheit ke celcius:'))
fahrenheit - 32 * 9/5
print(fahrenheit)

celcius=int(input('masukan suhu dari celcius ke fahrenheit'))
celcius= ((9/5) * celcius)+ 32
print(celcius)


# suhu = input('inputkan suhu celcius atau fahrenheit!')
# #mendapatkan char terakhir
# jenis=suhu[-1]

# #mendapatkan nilai selain karakter terakhir
# suhu= float(suhu[:-1])

# if jenis =='C':
#     #celcius ke fahrenheit
#    konversi=(suhu-32)*5/9

# elif jenis =='F':
#     #fahrenheit ke celcius
#     konversi = suhu*9/5 + 32

# print(f"Suhu asal{suhu}dikonversi menjadi:{konversi}")