
print(' \      PRISMA SEGITIGA '          )
print('='*30)
alas= float(input('inputkan alas: '))
tinggi= float(input('inputkan tinggi : '))
tinggi_prisma= float(input('inputkan tinggi prisma : '))
keliling_alas= float(input('inputkan keliling alas : '))

luas=(2*(1/2*alas*tinggi))+(keliling_alas*tinggi_prisma)
volume=(1/2*alas*tinggi)*tinggi_prisma

print(f'luas prisma segitiga adalah',luas,'cm2')
print(f'volume prisma segitiga adalah',volume,'cm2')