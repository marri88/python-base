# Напишите функцию которая спрашивает число N и 
# генерирует вам List состоящий из N разных элементов.

import random
def rand_numlist(a):
    k = []
    i = 0
    while i < a:
        k.append(random.randint(1,50))
        i+=1
    print(k)

a = int(input())
rand_numlist(a)



