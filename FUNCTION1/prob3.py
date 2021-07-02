# Создайте функцию сложения, затем функцию вычитания двух чисел...
# Создайте 3-ю функцию которая вызывает первые 2 внутри себя.


# def plus(a,b):
#     print(a + b)

# def minus(a,b):
#     print(a - b)

# def umnojenie(a,b):
#     print(a * b)

# def delenie(a,b):
#     print(a / b)

# def otvet(a,b):
#     plus(a,b)
#     minus(a,b)
#     umnojenie(a,b)
#     delenie(a,b)

# #вести значение a  и  b 
# otvet(150,150) 


#version 1
# def sum(a,b):
#     print(a+b)
# def minus(a,b):
#     print(a-b)
# def minusplus():
#     sum(2,4)
#     minus(5,1)
# minusplus()


#version 2

# def calculate():
#     operation=input("'+' or '-'")
#     number_1 = int(input("First number: "))
#     number_2 = int(input("Second number: "))
#     if operation == "+" :
#         print("{} + {} = ".format(number_1, number_2))
#         print(number_1 + number_2)
#     elif operation == "-" :
#         print("{} - {} = ".format(number_1, number_2))
#         print(number_1 - number_2)
# calculate()


#version 3

# a=int(input("vvedite a"))    
# b=int(input("vvedite b"))
def f1(a,b):
  a+b

def f2(a,b):
  a-b

def f3(a,b):
  if a <=10:
    f1(a,b)
  else:
    f2(a,b)
c = f3(5,2)
print(c)