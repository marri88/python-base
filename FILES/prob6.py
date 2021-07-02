# Создайте форму регистрации которая спрашивает у пользователя: 
# Логин, Пароль и Фото. Заранее подготовьте фото на компьютере и 
# когда программа спросит ваше фото просто укажите полный путь 
# до места где лежит ваше фото. Программа должна проверить если 
# фото правда существует по такому пути И также это фото с одним 
# из 3 расширений("jpeg", "jpg", "png") то вы сохраняете
#  в файл логин, пароль, путь до фото которое указал пользователь. 
# А самому пользователю вы говорите о том что Регистрация Успешна!



f = open('/home/aimira/python/python3/week2files/p.png', 'rb')
login = input("login: ")
password = input("password: ")
picture = input("path to picture: ")
k = open(picture, 'rb')

if f.read() == k.read():
	h = open('/home/aimira/python/python3/week2files/users.txt', 'w')
	h.write(f"Login: {login}\nPassword: {password}\nPut': {picture}")
	print('Регистрация Успешна')
	h.close()
f.close()
k.close()
