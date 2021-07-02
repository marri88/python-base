# Написать Функцию которая принимает предложение как аргумент, 
# считает количество букв и возвращает сколько символов он ввёл. 
# НЕ ИСПОЛЬЗОВАТЬ функцию len()

def func(str):
    counter = 0    
    for i in str:
        counter += 1
    return counter
str = "qwerty fqwerty qwert fghsdjk"
print(func(str))

#version 1
# def word_sum(a):
#     c = 0
#     for x in a:
#         if ('a' <= x <= 'z') or ('A' <= x <= 'Z') or ('а' <= x <= 'я') or ('А' <= x <= 'Я'):
#             c += 1
#         else:
#             pass
#     print(c)

# a = input()
# word_sum(a)