# Создайте функцию которая генерирует 10 чисел Фибоначчи: 
# 1,1,2,3,5,8,13,21,34,...


def fibo():
    i = 0
    a = 1
    b = 1
    fib = [a, b]
    while i < 10:
        c = a + b
        a = b
        b = c
        fib.append(c)
        i += 1
    print(fib)      
fibo()


#version 1
# def fib(lowerbound,upperbound):
#     x=0
#     y=1
#     while x<= upperbound:
#             if(x >= lowerbound):
#                     yield x
#             x, y = y, x + y
# startNumber=0
# endNumber=10

# for fib_sequence in fib(startNumber, endNumber):
#     print(fib_sequence)




# version 2
# def fibonachi():
#     fib1=fib2=1
#     n=int(input())
#     if n<2:
#         quit()
#     print(fib1, end='')
#     print(fib2, end='')
#     for i in range(2, n):
#         fib1,fib2=fib2,fib1+fib2
#         print(fib2, end='')
# fibonachi()