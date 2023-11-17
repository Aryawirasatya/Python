
print('            RUMUS BALOK                 ')
print('=======================================')
p = int(input('\tmasukan panjang balok:\t'))
l = int (input('\tmasukan lebar balok:\t'))
t = int (input('\tmasukan tinggi balok:\t'))

L = 2 * ( p*l + p*t + l*t )
V = p*l*t

print('\tLuas :',str(L),'cm2')
print('\tvolume:',str(V),'cm3')
