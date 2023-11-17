print('='*30)
print('\t LIMAS SEGITIGA')
t = float(input('masukan tinggi limas :'))
T = float(input('masukan tinggi:'))
a = float(input('masukan alas:'))

ls1 = float(input('LS1:'))
ls2 = float(input('LS2:'))
ls3 = float(input('LS3:'))
ls4 = float(input('LS4:'))

luas_alas= ls1 + ls2 + ls3 + ls4
volume = 1/6 * a * t * T


print('\tluas alas:',str(luas_alas),'cm2\t')
print('\tvolume:',str(volume),'cm3\t')
