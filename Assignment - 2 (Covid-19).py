age = input('Are you a cigarette addict older than 75 years old?').title().strip()
if age == 'Yes':
    age = True
elif age == 'No':
    age = False
else:
    print('Hatalı giriş yaptınız. lütfen sorulara Yes/No şeklinde cevap verirmisiniz')
    
chronic = input('Do you have a severe chronic disease?').title().strip()
if chronic == 'Yes':
    chronic = True
elif chronic == 'No':
    chronic = False
else:
    print('lütfen sorulara Yes/No şeklinde cevap verirmisiniz')
    
immune = input('Is your immune system too weak?').title().strip()
if immune == 'Yes':
    immune = True
elif immune == 'No':
    immune = False
else:
    print('lütfen sorulara Yes/No şeklinde cevap verirmisiniz')
    
if (age or chronic or immune) == False:
    print('You are not in risky group')
else:
    print('You are in risky group')