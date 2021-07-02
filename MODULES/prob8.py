# Спросите у пользователя 2 значения через input() а затем через модуль sys проверьте какое из 2-х значений занимает больше памяти.

import sys 
x = input()
y = input()
# print(sys.getsizeof({x}, {y}))
if sys.byteorder({x}) > sys.byteorder({y}):
	print("x>y")
elif sys.byteorder({y}) > sys.byteorder({x}):
	print("y>x")
