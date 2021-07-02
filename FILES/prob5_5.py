# Создайте database.txt файл с несколькими логинами и паролями. 
# Затем попросите пользователя войти или зарегистрироваться. 
# Спросите его логин и пароль. 
# Если такой логин уже есть скажите ему что логин уже существует и предложите зарегистрироваться спросив пароль. 
# Если такого логина неоказалось среди уже существющих продолжайте регистрацию. 
# Спросите у него Пароль 2 раза и сохраните в в файл datebase.txt только если пароли совпадают.
while True:
	print('''войти или зарегистрироваться
		1 - Войти
		2 - Зарегистрироваться''')

	a = input('введите ваш ответ: ')
	if a == '1':
		login = input("логин: ")
		password = input("пароль: ")
		r = open('/home/aimira/python/python3/week2files/datebase.txt', 'r')
		if login in r.read():
			print('такой логин уже существует')
			login = input("логин: ")
			password = input("пароль: ")
			password1 = input("потвердите пароль: ")
			if password == password1:
				r = open('/home/aimira/python/python3/week2files/datebase.txt', 'a')
				r.write(f"name: {login}, password: {password}")
				r.close()
			else:
				while password != password1:
					print('введите пароль еще раз')
					password = input("пароль: ")
					password1 = input("потвердите пароль: ")
				r = open('/home/aimira/python/python3/week2files/datebase.txt', 'a')
				r.write(f"name: {login}, password: {password}")
				r.close()
		else:
			r = open('/home/aimira/python/python3/week2files/datebase.txt', 'a')
			r.write(f"name: {login}, password: {password}")
			r.close()
	if a == '2':
		login = input("логин: ")
		password = input("пароль: ")
		password1 = input("потвердите пароль: ")
		r = open('/home/aimira/python/python3/week2files/datebase.txt', 'r')
		if login in r.read():
			print('Polzovatel uzhe est, vvedite drugoi login!')
			login = input("логин: ")
			password = input("пароль: ")
			password1 = input("потвердите пароль: ")

		if password == password1:
			r = open('/home/aimira/python/python3/week2files/datebase.txt', 'a')
			r.write(f"name: {login}, password: {password}")
			r.close()
		else:
			while password != password1:
				print('введите пароль еще раз')
				password = input("пароль: ")
				password1 = input("потвердите пароль: ")
			r = open('/home/aimira/python/python3/week2files/datebase.txt', 'a')
			r.write(f"name: {login}, password: {password}")
			r.close()





	