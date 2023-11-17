# for x in range(1,10,2):
#     print(x)

# print('===============')
# # 1
# for x in range(0,101,2):
#     print(x)

# print('===============')
# # 2
# for x in range(10,101,10):
#      print(x)

# print('===============')
# # 3
# for x in range(1,11):
#     print(x,'x')

# print('===============')
# # 4
# for x in range(1,11):
#     print('hello',x)


# for x in range(1,6):
#     print(f'{x} * {x+1} = {x * (x+1)}')

# for x in range(10,1,-1):
#       print(x,end =' ')

   



# teks = 'hello'
# print(teks[4])
# print(len(teks))
# for x in range (len(teks)-1,-1,-1):
#     print(teks[x], end=' ')


# ======================= #
  #        while          #

# i = 0 #inisialisasi =pemberian nilai awal
# while i  <= 100: # kondisi = while akan berjalan bila nilai kondisinya benar,
#    print(i, end = ' ') if i%2 == 0 else print('', end='')
#    i += 2 #kondisi terakhir pengulangan

# #===========================#

# i = 0 #inisialisasi =pemberian nilai awal
# while i  <= 100: # kondisi = while akan berjalan bila nilai kondisinya benar,
#    print(i, end = ' ') if i%5 == 0 and i%20 == 0 else print('', end='')
#    i += 2 #kondisi terakhir pengulangan

# i = 1
# jumlahhhh = 0 
# while i <= 10:
#    i += 1
# print(jumlahhhh)
# i = 1
# while i <= 10:
#     print(i,'+',end='')
#     i +=1


# i=5
# teks=''
# jumlah= 0
# while i >= 1:
#     teks += str(i)
#     teks += '+' if(i>1) else "="
#     jumlah += i
#     i-=1

# print(teks,jumlah)


# q = input('Apakah mau diulang(y/n)?')

# while q != 'n':
#     q =input ('Apakah mau diulang(y/n)?')



t = int(input('masukan tinggi segitiga siku-siku : '))
 
for i in range (1,t + 1):
  print((t - i + 1) *'*') 