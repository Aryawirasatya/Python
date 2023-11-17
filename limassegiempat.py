print('          LIMAS SEGIEMPAT         ')
print('—' *30)
t = float(input('masukan tinggi limas:'))
la = float(input('masukan luas alas:'))
ls1 = float(input('LS1:'))
ls2 = float(input('LS2:'))
ls3 = float(input('LS3:'))
ls4 = float(input('LS4:'))
ls5 = float(input('LS5:'))



luas_permukaan =  ls1 + ls2 + ls3 + ls4 + ls5
volume         = (1/3) *la * t

print('\tluas permukaan:',str(luas_permukaan),'cm2\t')
print('\tvolume:',str(volume),'cm3\t')
