



# user_data = [{
#   "id": 1,
#   "first_name": "Humphrey",
#   "last_name": "Wilcox",
#   "email": "hwilcox0@odnoklassniki.ru",
#   "gender": "Male",
#   "ip_address": "80.232.175.95"
# }, {
#   "id": 2,
#   "first_name": "Erhard",
#   "last_name": "Byart",
#   "email": "ebyart1@addthis.com",
#   "gender": "Male",
#   "ip_address": "125.7.237.155"
# }, {
#   "id": 3,
#   "first_name": "Brok",
#   "last_name": "Leiden",
#   "email": "bleiden2@usnews.com",
#   "gender": "Male",
#   "ip_address": "108.201.248.102"
# }, {
#   "id": 4,
#   "first_name": "Gradeigh",
#   "last_name": "Spreckley",
#   "email": "gspreckley3@marriott.com",
#   "gender": "Male",
#   "ip_address": "90.169.195.245"
# }, {
#   "id": 5,
#   "first_name": "Trueman",
#   "last_name": "McArd",
#   "email": "tmcard4@cargocollective.com",
#   "gender": "Male",
#   "ip_address": "249.26.239.198"
# }, {
#   "id": 6,
#   "first_name": "Giacobo",
#   "last_name": "Rishworth",
#   "email": "grishworth5@merriam-webster.com",
#   "gender": "Male",
#   "ip_address": "156.104.68.219"
# }, {
#   "id": 7,
#   "first_name": "Marcia",
#   "last_name": "Burney",
#   "email": "mburney6@gmpg.org",
#   "gender": "Female",
#   "ip_address": "52.104.185.232"
# }, {
#   "id": 8,
#   "first_name": "Court",
#   "last_name": "Haysar",
#   "email": "chaysar7@eepurl.com",
#   "gender": "Hidden",
#   "ip_address": "60.138.180.175"
# }, {
#   "id": 9,
#   "first_name": "Penn",
#   "last_name": "Slatten",
#   "email": "pslatten8@narod.ru",
#   "gender": "Male",
#   "ip_address": "216.91.212.228"
# }, {
#   "id": 10,
#   "first_name": "Rayna",
#   "last_name": "Jacobsson",
#   "email": "rjacobsson9@4shared.com",
#   "gender": "Female",
#   "ip_address": "158.81.126.17"
# }, {
#   "id": 11,
#   "first_name": "Elissa",
#   "last_name": "Milch",
#   "email": "emilcha@ucoz.ru",
#   "gender": "Female",
#   "ip_address": "160.46.17.104"
# }, {
#   "id": 12,
#   "first_name": "Cissiee",
#   "last_name": "Dever",
#   "email": "cdeverb@dailymail.co.uk",
#   "gender": "Hidden",
#   "ip_address": "198.12.171.92"
# }, {
#   "id": 13,
#   "first_name": "Lorie",
#   "last_name": "Cavozzi",
#   "email": "lcavozzic@apache.org",
#   "gender": "Female",
#   "ip_address": "252.228.114.151"
# }, {
#   "id": 14,
#   "first_name": "Shelton",
#   "last_name": "Pipe",
#   "email": "spiped@opera.com",
#   "gender": "Male",
#   "ip_address": "217.193.203.141"
# }, {
#   "id": 15,
#   "first_name": "Cordell",
#   "last_name": "Hrinchenko",
#   "email": "chrinchenkoe@ovh.net",
#   "gender": "Transgender",
#   "ip_address": "147.76.167.191"
# }, {
#   "id": 16,
#   "first_name": "Dyanna",
#   "last_name": "Sizzey",
#   "email": "dsizzeyf@xing.com",
#   "gender": "Female",
#   "ip_address": "8.177.20.12"
# }, {
#   "id": 17,
#   "first_name": "Felice",
#   "last_name": "Floyed",
#   "email": "ffloyedg@instagram.com",
#   "gender": "Male",
#   "ip_address": "4.150.254.58"
# }, {
#   "id": 18,
#   "first_name": "Arel",
#   "last_name": "Donoher",
#   "email": "adonoherh@youtu.be",
#   "gender": "Male",
#   "ip_address": "186.214.243.230"
# }, {
#   "id": 19,
#   "first_name": "Kristoffer",
#   "last_name": "Carvill",
#   "email": "kcarvilli@xinhuanet.com",
#   "gender": "Male",
#   "ip_address": "58.204.72.103"
# }, {
#   "id": 20,
#   "first_name": "Norbie",
#   "last_name": "Oleksinski",
#   "email": "noleksinskij@free.fr",
#   "gender": "Male",
#   "ip_address": "242.192.49.216"
# }]



### Решение Хакатона: ###

# Task 1:
# class Cesar:
#   def init(self,slovo):
#     self.slovo = slovo
#     self.encoded_slovo = ''     # Строка куда мы будем записывать ЗАШИФРОВАННЫЕ буквы.
#     self.decoded_slovo = ''     # Строка куда мы будем записывать РАСШИФРОВАННЫЕ буквы.


#   def encode(self):
#     slovo_in_list = tuple(self.slovo)
#     for bukva in slovo_in_list:
#       self.encoded_slovo += chr(ord(bukva) + 7)
#     #   print('До шифрования', bukva, '-', ord(bukva))
#     #   print('После шифрования', chr(ord(bukva) + 7), '-', ord(bukva) + 7)
#     #   print()
#     return self.encoded_slovo


#   def decode(self):
#     slovo_in_list = tuple(self.slovo)
#     for bukva in slovo_in_list:
#       self.decoded_slovo += chr(ord(bukva) - 7)

#     return self.decoded_slovo

# cesar = Cesar('Olssv')
# print(cesar.encode())
# print(cesar.decode())


# Task 2:
# Решение 1:
# import datetime

# class Logger:
#   def init(self, login):
#     self.login = login


#   def registration(self):
#     if len(self.login) < 5:
#       return 'Логин слишком короткий!'

#     return self.check_passwords()


#   def check_passwords(self):
#     password_1 = input('Введите Пароль: ')

#     while True:
#       if len(password_1) < 8:
#         print("Пароль слишком короткий!\n")
#         password_1 = input('Введите Пароль: ')

#       else:
#         password_2 = input('Подтвердите Пароль: ')

#         if password_1 == password_2:
#           break

#         else:
#           print("Пароли не совпадают!\n")
#           password_1 = input('Введите Пароль: ')

#     with open('/home/<user>/Desktop/users.txt', 'a') as users:
#       users.write(f'Логин:{self.login} - Пароль:{password_1}\n')

#     with open('/home/<user>/Desktop/log.txt', 'a') as users:
#       users.write(f'Пользователь успешно зарегистрирован {datetime.datetime.now().time()}')
        
#     return f'Пользователь {self.login} : {password_1} успешно зарегистрирован {datetime.datetime.now().time()}'


# user_loggin = input('Введите логин: ')

# logger = Logger(user_loggin)
# print(logger.registration())


# # Решение 2:
# def registration(login):
#   if len(login) < 5:
#       return 'Логин слишком короткий!'
#   else:
#     password_1 = input('Введите Пароль: ')

#     while True:
#       if len(password_1) < 8:
#         print("Пароль слишком короткий!\n")
#         password_1 = input('Введите Пароль: ')

#       else:
#         password_2 = input('Подтвердите Пароль: ')

#         if password_1 == password_2:
#           break

#         else:
#           print("Пароли не совпадают!\n")
#           password_1 = input('Введите Пароль: ')

#     with open('/home/<user>/Desktop/users.txt', 'a') as users:
#       users.write(f'Логин:{login} - Пароль:{password_1}\n')

#     with open('/home/<user>/Desktop/log.txt', 'a') as users:
#       users.write(f'Пользователь успешно зарегистрирован {datetime.datetime.now().time()}')
        
#     return f'Пользователь {login} : {password_1} успешно зарегистрирован {datetime.datetime.now().time()}'

# # print(registration(input("Введите Логин: ")))


# Решение 3:
# import datetime
# class Registrator:
#     def main(self):
#         login = input('Введите Логин(5 символов мин.): ')
#         while len(login) < 5:
#             print('Логин слишком короткий...')
#             login = input('Введите Логин(5 символов мин.): ')

#         password1 = input('Введите Пароль(8 символов мин.):')
#         while len(password1) < 8:
#             print('Пароль слишком короткий...')
#             password1 = input('Введите Пароль(8 символов мин.):')

#         password2 = input('Подтвердите Пароль(8 символов мин.):')
#         while password1 != password2:
#             print('Пароли не совпадают!')
#             password1 = input('Введите Пароль(8 символов мин.):')
#             password2 = input('Подтвердите Пароль(8 символов мин.):')

#         with open('/home/azatot/Desktop/users.txt', 'a') as users:
#             users.write(f'Логин: {login} - Пароль: {password2}\n')
        
#         date_now = datetime.datetime.strftime(datetime.datetime.now(),'%H:%M:%S.%s')

#         with open('/home/azatot/Desktop/log.txt', 'a') as log:
#             log.write(f'Пользователь успешно зарегистрирован {date_now}\n')

# registrator = Registrator()
# registrator.main()

# # Task 3:
# class Parser:
#   def init(self,data):
#     self.data = data
#     self.genders_list = set()
#     self.domain_names = set()


#   def genders(self):
#     for user in self.data:
#       self.genders_list.add(user.get("gender"))

#     return tuple(self.genders_list)


#   def get_domain(self):
#     for user in self.data:
#       user_email = user.get("email")
#       user_domain = user_email.split('@')[1]

#       self.domain_names.add(user_domain)

#     return tuple(self.domain_names)

# parser = Parser(user_data)
# # print(parser.genders())
# # print(parser.get_domain())


# # Task 4:
# data_set = {('login', 'password', 'codeword'), 1988, 32, 'Python', 'Kyrgyzstan', ('October', 'November', 'December'), 'Senior', 'TeamLead'}

# def recursion(data_set):
#   if len(data_set) == 0:
#     return data_set

#   else:
#     new_data_set = list(data_set)

#     print(new_data_set)
#     print(new_data_set[-1])
#     print()
#     new_data_set.pop(-1) # Удаление по ИНДЕКСУ, НЕ по значению!
#     recursion(new_data_set)

# # recursion(data_set)


# Решени 2:
# def recursion(data):
#     print('Пришёл вот такой SET', data, 'его тип данных', type(data))
#     sequence = list(data)

#     if len(sequence) == 0:
#         return sequence

#     else:
#         new_sequence = sequence.pop(-1)
#         print(new_sequence)
#         return recursion(sequence)


# data_set = {('login', 'password', 'codeword'), 1988, 32, 'Python', 'Kyrgyzstan', ('October', 'November', 'December'), 'Senior', 'TeamLead'}
# recursion(data_set)



# # Task 5:
# def world():
#   return "Hello World"

# def kyrgyzstan():
#   return "Hello Kyrgyzstan"

# def bishkek():
#   return "Hello Bishkek"

# try:
#   user_function = input("Какую функцию запустить: ")
#   function = eval(user_function)() # Круглые скобки нужны для того чтобы функцию запустить, иначе пользователь должен в терминале написать: world(), bishkek()

#   print(function)
# except NameError:
#   print("Такой Функции нет!")



# # Task 6:
# from datetime import datetime, timedelta

# def schedule(date):
#   try:
#     user_date = datetime.strptime(date, "%Y-%m-%d %H:%M")

#     if str(user_date)[8:10] in ('05', '12', '19', '26'):
#       return f'Филиалы будут доступны {user_date + timedelta(hours=60)}'

#     else:
#       return 'Добро пожаловать! Мы открыты!'

#   except ValueError:
#     return "Неверный Формат Даты"

# schedule(input("Введите дату: "))



# # Task 7:
# def linux_commands():
#   commands = ('ls', 'mkdir', 'rm', 'move', 'cp', 'nano', 'touch', 'cat', 'date', 'pwd')
#   return commands

# l_c = linux_commands()

# del linux_commands