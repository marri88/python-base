a=17391%17
b=546%17
c=934%17
if a<b and a<c:
	print(a)
elif b<a and b<c:
	print(b)
elif c<a and c<b:
	print(c)
else:
	print("нет")
'''Есть три числа 17391, 546, 934.
Если каждое из них поделить на 17 по модулю, где остаток меньше всего? '''
print(a, b ,c)