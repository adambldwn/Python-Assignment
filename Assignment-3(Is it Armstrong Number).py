sayi = input('bir sayı giriniz')
sayi_list = list(sayi)
toplam = 0
if sayi.isdigit():
    for i in range(len(sayi_list)):
        toplam += (int(sayi_list[i])**len(sayi_list))
    if toplam == int(sayi):
        print(f'{sayi} Armstrong sayıdır')
    else:
        print(f'{sayi} Armstrong sayı degildir')    
else:
    print('Geçersiz bir giriş.lütfen pozitif tam sayı giriniz')