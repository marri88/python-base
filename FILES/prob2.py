# -week_2:Работа С файлами-
#####################################################################################
 # first picture: prob №2
 # Создайте файл users.txt. 
 # Напишите программу которая спрашивает у пользователя его Логин и Пароль и записывает в файл users.txt.
 
r = open('/home/aimira/python/python3/week2files/users.txt', 'w')
a = input("name: ")
b = input("password: ")
r.write(f"name: {a}, password: {b}")
r.close

with open('users.txt', 'r') as c:
    print(c.read())