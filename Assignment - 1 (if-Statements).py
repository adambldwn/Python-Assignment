name = 'efe'
parola = "W@12"

user = input('isminizi giriniz : ').lower().strip()
if user == name:
    print(f'Hello, {user}! The password is : W@12')
else:
    print(f'Hello, {user}! See you later.')