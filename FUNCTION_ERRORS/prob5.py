# Напишите код где есть TypeError,IndexError,NameError.

values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
b=('disana')
l = []
try:
    l.append(set(values(b)))
    print(l)
except SyntaxError: 
    print ("Ошибка")
except TypeError: 
    print(',,,,')
except NameError:
    print(",,,,")