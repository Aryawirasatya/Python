print('\tTRUMUS KERUCUT')
print('='*30)
s = float(input('masukan sisi:'))
r = float(input('masukan jari jari:'))
t = float(input('masukan tinggi:'))
PHI = 3.14

luas_selimut = PHI * r * s
luas_permukaan = PHI * r * s + PHI * r**2
volume = 1/3 * PHI * r**2 * t


print('\tluas permukaan:',str(luas_permukaan),'cm2\t')
print('\tluas selimut:',str(luas_selimut),'cm2\t')
print('\tvolume:',str(volume),'cm3\t')
