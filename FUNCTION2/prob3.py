# Напишите функцию которая принимает 2 
# Dictionary и добавляет втрорую Dictionary к первой.

def dic(a,b):
    a.update(b)
    print(a)

a = {input(''): input()}
b = {input(''): input()}

dic(a,b)


