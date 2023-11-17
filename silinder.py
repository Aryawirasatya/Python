print('\tRUMUS SILINDER\t')
print('='*30)
r = float(input('masukan jari jari:'))
t = float(input('masukan tinggi:'))

PHI = 3.14

luas_selimut = 2 * PHI * r * t
luas_permukaan = 2 * PHI * r * t + PHI * r**2
volume = PHI * r**2 * t

print('\tluas selimut:',str(luas_selimut),'cm2\t')
print('\tluas permukaan:',str(luas_permukaan),'cm2\t')
print('\tvolume:',str(volume),'cm3\t')