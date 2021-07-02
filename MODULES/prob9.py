# Создайте программу которая спрашивает у пользователя 
# число N для генерации пароля а затем 
# генерирует ему пароль длиною N символов.


import secrets
 
symbols = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789'
a = int(input("Сколько символов в паролей? "))
b = int(input("Сколько паролей? "))
count = 0
passlist = []
while count < b:
    while True:
        password = ''.join(secrets.choice(symbols) for i in range(a))
 
        if (any(c.islower() for c in password) and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)):
            break
    count += 1
    passlist.append(password)
print(passlist)


