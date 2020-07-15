fibonacci = [1,1]
i = 0
toplam = 0
while toplam < 55:
    toplam = fibonacci[i] + fibonacci[i+1]
    fibonacci.append(fibonacci[i] + fibonacci[i+1])
    i +=1
    
print(fibonacci)