# Напишите программу которая выводит только нечётные числа с помощью рекурсии.

def func(num):
    print(num)
    if num % 2 == 0:
        return num 
    else:
        func(num + 2)
func(1)