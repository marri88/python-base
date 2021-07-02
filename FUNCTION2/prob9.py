# Напишите функцию которая принимает 2 аргумента. 
# Эти аргументы могут быть любого типа данных но функция должна 
# Вам вернуть эти аргументы как тип данных List.

def list_1(a,b):
    i = []
    i.append(a)
    i.append(b)
    print(i)

a = input()
b = input()
list_1(a,b)


#ver1
def twoargs(a, b):
    list1 = []
    list1.append(a)
    list1.append(b)
    print(list1)
twoargs(911, 'support')