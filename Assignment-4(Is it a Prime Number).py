sayi = int(input('bir sayı giriniz'))
a = 0
for i in range(2, sayi):
    if sayi % i == 0:
        a +=1
        break
if a == 0:
    print(f'{sayi} asal sayıdır')
else:
    print(f'{sayi} asal sayı değildir')