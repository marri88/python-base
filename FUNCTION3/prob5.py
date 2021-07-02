# Напишите функцию которая генерирует 100 рандомных чисел в диапазоне от 10 до 50 и возвращает их в листе. 
# Напишите ДЕКОРАТОР для этой функции которая удалит все дубликаты в первой функции и вернёт всё так же лист.

 import random
def kk(kuff):
    n = []
    for x in kuff():
        if x not in n:
            n.append(x)
    print(n)
@kk
def gg():
    l = []
    for i in range(100):
        a = random.randint(10,50)
        l.append(a)
    return l
