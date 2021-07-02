# Chapter 4

# 1)Student
# Создайте класс Student, конструктор которого имеет параметры name, lastname,
# department, year_of_entrance. Добавьте метод get_student_info, который
# возвращает имя, фамилию, год поступления и факультет в
# отформатированном виде: “Вася Иванов поступил в 2017 г. на факультет:
# Программирование.”

# class Student():
#     def __init__(self,name,last_name,department,year_of_entrance):
#         self.name = name
#         self.last_name =last_name
#         self.department = department
#         self.year_of_entrance = year_of_entrance
#     def get_student_info(self):
#         return f"{self.name} {self.last_name} поступил на факультет {self.department} в {self.year_of_entrance} году"

# student1 = Student("Иван","Иванов","Программирования""2017")
# print(student1.get_student_info())

# 2)Airplane
# Создайте новый класс Airplane. Создайте следующие характеристики (полей)
# объекAта:
# ● make (марка)
# ● model
# ● year
# ● max_speed
# ● odometer
# ● is_flying
# и методы имитирующих поведение самолета take off (взлет), fly (летать), land
# приземление). Метод take off должен изменить is_flying на True, а land на False. По
# умолчанию поле is_flying = False. Метод fly должен принимать расстояние полета и
# изменять показания одометра (километраж). Создайте 1 объект класса и используйте
# все методы класса.

# class Airplane():
#     def __init__(self,model,year,max_speed,odometer = 0,is_flying = False):
#         #self.make = make
#         self.odometer = 0
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed

#     def take_off(self):
#         self.is_flying = True
#         print(f'Самолет {self.model} взлетел, скорость {self.max_speed} км/ч, расстояние  {self.odometer}')

#     def fly(self):
#         self.odometer += 100
           
#     def land(self):
#         self.is_flying = False


# samolet = Airplane(
#     model = "Boing 777",
#     year = '2020',
#     max_speed = 600)

# samolet.fly()
# samolet.take_off()



# 3)Car
# Создайте класс Car. Пропишите в конструкторе параметры make, model, year,
# odometer, fuel. Пусть у показателя odometer будет первоначальное значение 0,
# а у fuel 70. Добавьте метод drive, который будет принимать расстояние в км. В
# самом начале проверьте, хватит ли вам бензина из расчета того, что машина
# расходует 10 л / 100 км (1л - 10 км) . Если его хватит на введенное расстояние,
# то пусть этот метод добавляет эти километры к значению одометра, но не
# напрямую, а с помощью приватного метода __add_distance. Помимо этого
# пусть метод drive также отнимет потраченное количество бензина с помощью
# приватного метода __subtract_fuel, затем пусть распечатает на экран “Let’s
# drive!”. Если же бензина не хватит, то распечатайте “Need more fuel, please, fill
# more!”

# class Car():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = 0
#         self.fuel = 70
    
    
#     def add_distance(self,km):
#         self.odometer += km
        

#     def subtract_fuel(self,km):
#         self.fuel -= km/10
    
#     def drive(self,km):
#         result = km / 10
#         if result <= 70:
#             self.add_distance(km)
#             self.subtract_fuel(km)
#             print(f"Let's go drive!,{self.make}--{self.model}--{self.year} year\n Расстояние - {self.odometer} км \n Остаток  бензина - {self.fuel} л")
#         else:
#             print('“Need more fuel, please, fill more!”')


# c = Car(
#     make = 'Tayota',
#     model = 'Wish',
#     year = 2005)

# c.drive(500)
# c.add_distance(500)



# 4)ContactList
# Создайте класс ContactList, который должен наследоваться от
# встроенного класса list. В нем должен быть реализован метод
# search_by_name, который должен принимать имя, и возвращать список
# всех совпадений. Замените all_contacts = [ ] на all_contacts =
# ContactList(). Создайте несколько контактов, используйте метод
# search_by_name.

# class ContacList(list):
#     def __init__(self,*args):
#         self.novyi_list = []
#         for x in args:
#             self.novyi_list.append(x)

#     def search_by_name(self,name):
#         for x in self.novyi_list:
#             if x == name:
#                 print(f'{x}')
#             else:
#                 pass

# all_contacts = ContacList('Adilet','Ryspek','Sanjar','Alina','Adilet')
# all_contacts.search_by_name('Adilet')


# class ContactList:
#     def __init__(self,names):
#         self.names = names
#     def search_by_name(self,search):
#         for name in self.names:
#             if name == search:
#                 print(name)
# all_contacts=ContactList(['Саша','Саша','Саша','Коля','Миша','Саша','Света','Никита','Миша',
#                 'Валера','Валера','Юля','Юля','Саша','Саша','Саша','Оля','Юля','Саша','Оля','Петя',
#                 'Петя','Юля','Антон','Антон','Маша','Гоша','Оля','Юля','Гоша','Оля','Юля'])
# all_contacts.search_by_name("Антон")



# 5)AK-47
# Soldier Ryan has an AK47
# Soldiers can fire ("tigi-tigitishh").
# Guns can fire bullets.
# Guns can fill bullets - increase the number of bullets(reloads)
# Create class Act_of_Shooting, which will inheritates from class Soldier, class Guns.
# Where soldier will fire from a gun and reload, and fire one more time.

# class Soldier():
#     def __init__(self, name, gun):
#         self.name = name
#         self.gun = gun

# class Guns():
#     def shoots(self):
#         print(f'{self.name} shoots from: {self.gun}')
#         self.ammunition = 30
#         while self.ammunition > 0:
#             self.ammunition -= 1
#             print('shot')

#         if self.ammunition == 0:
#             self.reloads()
#         else:
#             pass


#     def reloads(self):
#         self.reload = input('reload weapson? y/n: ')
#         if self.reload == 'y':
#             self.shoots()
#         else:
#             pass


# class Act_of_Shooting(Soldier, Guns):
#     def __init__(self, name, gun):
#         Soldier.__init__(self, name, gun)


# soldier1 = Act_of_Shooting('Ryan', 'AK47')
# soldier1.shoots()



# import time
# class Soldier:
#     def __init__(self, name):
#         self.name = name
    
# class Guns:
#     def __init__(self, bullets, magazine):
#         self.bullets = bullets
#         self.magazine = magazine
#     def pih_pah(self):
#         for i in range (self.magazine):
#             for x in range (self.bullets):
#                 print("tigi-tigitishh")
#                 time.sleep(0.3)
#             if i != 1:
#                 print("Перезаряжаюсь!")
#                 time.sleep(3)
#             else:
#                 print("Патронов нет!")
                
# class Act_of_shooting(Soldier, Guns):
#     def __init__(self, name, bullets, magazine):
#         Soldier.__init__(self, name)
#         Guns.__init__(self, bullets, magazine)
        
# a=Act_of_shooting("sdf", 2, 2)
# a.pih_pah()

# class Soldier:

#     def __init__(self, name, model_of_weapon):
#         self.name = name
#         self.model_of_weapon = model_of_weapon



# class Act_of_Shooting(Soldier):

#     def __init__(self, name, model_of_weapon):
#         self.name = name
#         self.model_of_weapon = model_of_weapon


#     def fire(self):
#         print('{} tigi-tigitishh'.format(self.name))

#     def guns_fire(self):
#         print('{} fire bullets'.format(self.model_of_weapon))

#     def fill_bullets(self, numb_of_bullets):
#         print('{} reloads {} bullets'.format(self.name,numb_of_bullets))

# ryan = Act_of_Shooting('Ryan', 'AK47')
# ryan.fire()
# ryan.guns_fire()
# ryan.fill_bullets(20)


# 6)Furniture:
# Household type, total area and furniture name listThe new house has no furniture at all.
# Furniture has a name and area, of whichBed: 4 square metersWardrobe: 2 square metersTable: 1.5 square meters
# Add the above three pieces of furniture to the house
# When printing a house, output is required: household type, total area, remaining area, furniture name list.

# class House():
#     def __init__(self, typehouse, areahouse):
#         self.typehouse = typehouse
#         self.areahouse = areahouse

#     def get_house(self):

#         self.totalarea = 0
#         self.furnitures = {
#             'bed' : 4,
#             'wardrobe' : 2,
#             'table' : 1.5
#         }
#         for value in self.furnitures.values():
#             self.totalarea += value
        

#         print(f'Type: {self.typehouse} -- Total Area: {self.areahouse}\n{list(self.furnitures.keys())}\nArea: {self.areahouse - self.totalarea}')

        
# var1 = House('Kvartira', 80)
# var1.get_house()




# class House:
#     def __init__(self, type_, total_area, names_furniture):
#         self.type = type_
#         self.total_area = total_area
#         self.names_furniture = names_furniture
#         self.remaining_area = total_area
#     def cali(self):
#         for furniture in self.names_furniture:
#             if furniture == 'Bed':
#                 self.remaining_area -= 4
#             elif furniture == 'Wardrobe':
#                 self.remaining_area -= 2
#             elif furniture == 'Table':
#                 self.remaining_area -= 1.5
#         print(f'household type: {self.type} total area: {self.total_area} \nremaining area: {self.remaining_area} furniture name: {self.names_furniture}')
# house_1=House("asd", 123, ['Bed', 'Wardrobe', 'Table']).cali()

# class HouseAimira():
#     def init(self, typehouse, areahouse):
#         self.typehouse = typehouse
#         self.areahouse = areahouse

#     def get_house(self):

#         self.totalarea = 0
#         self.furnitures = {
#             'bed' : 4,
#             'wardrobe' : 2,
#             'table' : 1.5
#         }
#         for value in self.furnitures.values():
#             self.totalarea += value
        

#         print(f'{self.typehouse} -- Total Area: {self.areahouse}\n{list(self.furnitures.keys())}\nArea: {self.areahouse - self.totalarea}')


# class NewHouse(HouseAimira):
#     pass

# # var1 = HouseAimira('Kvartiraaimira', 80)
# # var1.get_house()
# v = NewHouse('Flat', 90)
# v.get_house()

# class House():
#     '''Создание класса дома'''
#     def __init__(self,тип_дома, общая_площадь):
#         '''Инициализация атрибутов дома '''
#         self.тип_дома = тип_дома
#         self.общая_площадь = общая_площадь
#         self.спальня = 4
#         self.гардероб = 2
#         self.стол = 1.5

#     def __Area(self): # заприваченный метод
#         '''Стиль дома и общая площадь'''
#         print(f"Наш дом сделан в стиле {self.тип_дома} ,общаяя площадь у него {str(self.общая_площадь)}")

#     def Ост_Area(self):
#         '''Находим оставщуюся площадь'''
#         self.оставшаяся_площадь = self.общая_площадь - self.спальня - self.гардероб - self.стол
#         print(f"В нашем доме спальня занимает {str(self.спальня)} квадратных метра, гарнитур занимает {str(self.гардероб)} квадратных метра,и стол {str(self.стол)} квадратных метра, и оставщаяся площадь у нас {str(self.оставшаяся_площадь)} квадратных метра.")

# Кирпич = House('Кирпич',35)
# Кирпич._House__Area()
# Кирпич.Ост_Area()

# class New_House(House):
#     def __init__(self,тип_дома, общая_площадь):
#         super().__init__(тип_дома, общая_площадь)
        
# Фаверх = New_House('Фаверх',25)
# Фаверх._House__Area() #для того, чтобы наш приваченный метод увидел терминал,нам нужно после экземпляра через нижнюю черточку написать наш Класс и после заприваченый метод. 
# Фаверх.Ост_Area()

# 7)Students room:
# Implement Students room using OOP:
# Copy
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>

# class Student():
#     def __init__(self,name,age,major):
#         self.name = name
#         self.age = age 
#         self.major = major
    
#     def __repr__(self):
#         return (f'\nname--{self.name}-age-{self.age}-major-{self.major}')

# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")

# print(Penny)


# 8)Dollar
# Create function dollarize() that takes Float and returns dollarized format:
# Copy
# dollarize(123456.78901) -> "$123,456.80"
# dollarize(-123456.7801) -> "-$123,456.78"
# dollarize(1000000) -> "$1,000,000"
# Convert this function into useful class MoneyFmt. MoneyFmt contains single data value(the amount) and 4 methods.
# Copy
#     "init" //constructor initializes the data value
#     "update" //method replaces data value with new one
#     "repr" //methods returns Float value
#     "str" //method, that implements logic of dollarize() method
# Copy
# //The output will look like this:
# import moneyfmt
# cash = moneyfmt.MoneyFmt(12345678.021)
# print(cash) -- returns "$12,345,678.02"
# cash.update(100000.4567) 
# print(cash) -- returns "$100,000.46"
# cash.update(-0.3)
# print(cash) -- returns "-$0.30"
# repr(cash) -- returns -0.3

class MoneyFmt:
    def __init__(self, value=0.0): 
        self.value = float(value)
    def __str__(self):
        if self.value >= 0:
            return '${:,.2f}'.format(self.value)
        else:
            return '-${:,.2f}'.format(-self.value)
    def update(self, value=None):
        self.value=value
    def __repr__(self):
        print(self.value)
        return f'{self.value}'
cash = MoneyFmt(12345678.021)
cash.update(100000.4567)
cash.update(-0.3)
print(cash)
repr(cash)




# 9)Binary Search tree:
# https://www.getoutline.com/share/66b8b733-3e9b-4c72-938d-403ffa1d9f48
# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees

# 10)Complex Numbers
# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem?h_r=internal-search

# 12)Logger Decorator:﻿
# https://www.getoutline.com/share/63c5692f-51bb-4770-8047-566fac38bb95

# 13)Recursive digit sum:
# https://www.hackerrank.com/challenges/recursive-digit-sum/problem

# 14)Recursion: Davis Staircase(LRU cache)
# https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem




# 11)Exception Decorator
# ﻿https://www.getoutline.com/share/48d8609f-dd80-4796-8a32-a62800abf1cd﻿

# """Write a decorator that makes sure that only a particular type of exception is raised by the function.
# Tips:
#     Create class User with proper methods:
#         get_account_balance(),  change_password()
#         Create decorator to handle errors, listed below
# Input:
# u = User()
# u.get_account_balance()
# Output:
# Traceback (most recent call last):
#   File "main.py", line 159, in <module>
#     u.get_account_balance()
#   File "main.py", line 134, in wrapper
#     raise Exception("No username defined!")
# Exception: No username defined!
# Input:
# u = User()
# u.change_password()
# Output:
# Traceback (most recent call last):
#   File "main.py", line 159, in <module>
#     u.change_pasword()
#   File "main.py", line 134, in wrapper
#     raise Exception("No password to change!")
# Exception: No password to change!"""

# def excep(func):
#     def wrapper(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#         except TypeError as e:
#             print('!!!ошибка!!! ', e)
#     return wrapper

# class User:
#     @excep
#     def get_account_balance(self, username):
#         print("Hello "+ username)
#     @excep
#     def change_password(self, password):
#         print(password)

# u = User()
# u.get_account_balance("sdg")
# u.change_password(435)


# 15)Deck of Cards:
# Create a deck of cards class. Internally, the deck of cards should use another class, a card class. Your requirements are:

# The Deck class should have a deal method to deal a single card from the deck
# After a card is dealt, it is removed from the deck.
# There should be a "mix" method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# Класс карты должен иметь масть (червы, бубны, трефы, пики) и ценность (A, 2,3,4,5,6,7,8,9,10, J, Q, K)
# NOTE: use random shuffle
# Copy
# from random import shuffle

# from random import shuffle
# import random

# class Card:
#     def __init__(self,suit,val):
#         self.suit = suit
#         self.value = val
#     def show(self):
#         print('{}  {}'.format(self.value,self.suit))

# class Deck:
#     def __init__(self):
#         self.cards = []
#         self.build()
#     def build(self):
#         for s in ['Червы','Бубны','Трефы','Пики']:
#             for v in [2,3,4,5,6,7,8,9,10,'J', 'Q', 'K','A']:
#                 self.cards.append(Card(s,v))

#     def show(self):
#         for x in self.cards:
#             x.show()
#     def shuffle(self):
#         for i in range(len(self.cards)-1, 0, -1):
#             r = random.randint(0,i)
#             self.cards[i],self.cards[r] = self.cards[r], self.cards[i]

# deck = Deck()
# deck.shuffle()
# deck.show()


# 16) Герой.

# Разработайте программу по следующему описанию.
# В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный номер объекта, и свойство, в котором хранится принадлежность команде. У солдат есть метод "иду за героем", который в качестве аргумента принимает объект типа "герой".
# У героев есть метод увеличения собственного уровня.
# В основной ветке программы создается по одному герою для каждой команды. В цикле генерируются объекты-солдаты. Их принадлежность команде определяется случайно.
#  Солдаты разных команд добавляются в разные списки.
# Измеряется длина списков солдат противоборствующих команд и выводится на экран. У героя, принадлежащего команде с более длинным списком, поднимается уровень.
# Отправьте одного из солдат первого героя следовать за ним. Выведите на экран идентификационные номера этих двух юнитов.

# import random

# class unit: 
#     def __init__(self, n,team):
#         self.n=n
#         self.team=team
# class heroes(unit): 
#     def __init__(self,name,n,team,level=0):
#         self.name=name
#         self.level = level
#         self.team=team
#     def level_up(self, incr): 
#         self.level+=incr
 
# class soldier(unit): 
#     def follow_heroes(self,heroes):
#         print("\n"+"Для охраны своих владений герой {} выбрал опытного воина № {} и отправился с ним в поход.".format(heroes.name, self.n))
# Reychel,Molchanov=heroes("Reychel",1,"red"),heroes("Molchanov",2,"green") 
# red_team=[] 
# green_team=[] 
# quantity=int(input("Количество воинов:"))+1 
# for i in range(1,quantity): 
#     t=random.randint(0,1)
#     i=soldier(i,t)
#     if i.team==0:
#         red_team.append(i)
#         i.team="red"
#     else:
#         green_team.append(i)
#         i.team="green"
# if len(red_team)>len(green_team): 
#     Reychel.level_up(1)
# elif len(red_team)<len(green_team):
#     Molchanov.level_up(1)
# if len(red_team) >= 10:
#     Reychel.level_up(len(red_team) // 5)
# if len(green_team)>=10:
#     Molchanov.level_up(len(green_team)//5)
 
# print("В войске героя по имени",Reychel.name+",",str(Reychel.level)+"-го уровня,",len(red_team),"знатных воинов!")
# for i in red_team:
#     print(i.n, i.team, end=", ")
# print("\n"+"В войске героя по имени",Molchanov.name+",",str(Molchanov.level)+"-го уровня,",len(green_team),"знатных воинов!")
# for i in green_team:
#     print(i.n,i.team, end=", ")

# who=random.randint(0,1)
# if who==1:
#     t=red_team
#     h=Reychel
# else:
#     t=green_team
#     h=Molchanov
# random.choice(t).follow_heroes(h)

