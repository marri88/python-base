# # -week_2:Работа С файлами-
# ##################################################################################
# # second picture: prob №1

print('''зарегистрироваться
	yes      no ''')
q = input(':   ')
if q == 'yes':
	a = input("логин: ")
	b = input("пароль: ")
	r = open('/home/aimira/python/python3/week2files/datebase.txt', 'r')
	# for x in r:
	if a in r.read(): 
		print('такой логин уже существует.')
	elif a not in r.read(): 
		print('Продолжайте регистрацию')	
		r = open('/home/aimira/python/python3/week2files/datebase.txt', 'a')
		a = input("логин: ")
		b = input("пароль: ")
		c = input("потвердите пароль: ")
		if b == c:
			print('Реситрация прошло успешно')
		else:
			print('введите пароль еще раз')
			b = input("пароль: ")
			c = input("потвердите пароль: ")
			print('Реситрация прошло успешно')
		r.write(f"name: {a}, password: {b}")
		r.close()


# login1 = input("login")
# password1 = input("password")
# f = open('/home/aimira/python/python3/week2files/datebase.txt' , 'r')
# if login1 in f.read():
#   print("login ok")
#   f.close
# g = open('/home/aimira/python/python3/week2files/datebase.txt' , 'r')
# if password1 in g.read():
#   print("password ok")
#   g.close

# else:
#   print("nujan registraciya")
#   login2 = input("login")
#   password2 = input("password")
#   password22 = input("povtorite password")

#   c = open('/home/aimira/python/python3/week2files/datebase.txt' , 'r')
#   if login2 not in c.read():
#     if password2 not in c.read():
#       if password2 == password22:
#         c.close
#         i = open('/home/aimira/python/python3/week2files/datebase.txt' , 'a')
#         i.write(f"login: {login2}, password: {password2}")
#         i.close
#         print ("vse uspeshno")
#       else:
#         print('''vvedi parol eshe raz olen'!!!''')

# # nujen put' absolutnyi   






# # t = open ("database.txt", "w")
# # t.write("login : kamikadze , password : lololo , login: jojopa , password : hohoho , ")
# # t.close()
# # f = open("database.txt", "r")
# # x = (f.read().split())
# # n = input("Input login: ")
# # for i in range(int(len(x))):
# #     if x[i] == n:
# #         print("login is busy")
# #         log = input("input new login: ")
# #         pas = input("input new password: ")
# #         pas2 = input("repeat new passwort again: ")
# #         if pas == pas2:
# #             print("registrated new user")
# #             l = open("database.txt", "a")
# #             l.write(f"login : {log}, password : {pas},\n")
# #             l.close()
# #     else:
# #         pas = input("input new password: ")
# #         pas2 = input("repeat new passwort again: ")
# #         if pas == pas2:
# #             print("registrated new user")
# #             l = open("database.txt", "a")
# #             l.write(f"login : {log}, password : {pas},\n")
# #             l.close()
# #             break
# # f.close()







# # Создайте database.txt файл с несколькими логинами и паролями. 
# # Затем попросите пользователя войти или зарегистрироваться. 
# # Спросите его логин и пароль. 
# # Если такой логин уже есть скажите ему что логин уже существует и предложите зарегистрироваться спросив пароль. 
# # Если такого логина неоказалось среди уже существющих продолжайте регистрацию. 
# # Спросите у него Пароль 2 раза и сохраните в в файл datebase.txt только если пароли совпадают.