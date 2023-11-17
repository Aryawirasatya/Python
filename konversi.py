suhu = input('Inputkan suhu dalam Celcius atau Fahrenheit!')
# Mendapatkan char terakhir
jenis = suhu[-1].upper()

# Mendapatkan nilai selain karakter terakhir
suhu = float(suhu[:-1])

if jenis == 'C':
    # Celcius ke Fahrenheit
    konversi = suhu * 9/5 + 32

elif jenis == 'F':
    # Fahrenheit ke Celcius
    konversi = (suhu - 32) * 5/9

else:
    print("Jenis suhu tidak dikenal. Harap masukkan 'C' untuk Celcius atau 'F' untuk Fahrenheit.")
    konversi = None

if konversi is not None:
    print(f"Suhu asal {suhu} diubah menjadi: {konversi}")
