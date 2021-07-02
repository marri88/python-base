a = 600
while  a <= 600:
# 1
	if a > 99 and a < 1000:
		print('число трёхзначное')
	else:
		print("число не трёхзначное")
# 2
	if a > (-1):
		print('число положительное')
	else:
		print('число не положительное')
	if a % 2 == 0:
		print('число чётное')
	else:
		print('число не чётное')
# 3
	if a % 31:
		print('число делится на 31 без остатка')
	else:
		print('число не делится на 31 без остатка')
# 4
	if a > 100:
		print ('число больше 100')
	else:
		print('число не больше 100')
	if a % 17:
	     print ('число делится на 17')
	else:
		print('число не делится на 17')
	if a > 150: 
		print ('число больше 150')
	else:
		print('число не больше 150')
	if a == 13**2:
		print ('число равно на 13**2')
	else:
		print('число не равно на 13**2')
		break
print(a)
	
	# if ((a > 100 and a % 17) or (a > 150 and 13**2)):
	# 	print (a)
	# else:
# 	# 	print('4 условия не выполнено')


# d = int(input("chislo: "))
# ##1
# if (d >= 100) & (d < 1000):
#     print("Yes, trehznachnoe")
# else:
#     print("No, ne trehznachnoe")
# ##2
# if (d > 0) & (d%2==0):
#     print("Yes, polojitelnoe i chetnoe")
# else:
#     print("No, ne polojitelnoe ili(i) ne chetnoe")
# ##3
# if d%31==0:
#     print("Yes")
# else:
#     print("No")
# ##4
# if ((d > 100) & (d%17==0)) | ((d > 150) & (d==13**2)):
#     print(d)


'''num = 100
if(num < 1000 and num > 99):
    print("It's a 3 digit number")
else:
    print("is not a 3 digit number")

#3. Is it EVEN or ODD number?
if (num // 2) != 0:
    print("100 in an EVEN number")
else:
    print("100 is an ODD number")

#4 Can 100 be divided by 31 without remainder
if (num % 17) != 0 or (num > 150) and (num == 13**2):
    print(num)'''




# 8. Есть переменная которая хранит в себе число:
#    Необходимо написать следующие условия для проверки переменной:
#        1. Это число трёхзначное?
#        2. Это число положительное и чётное?
#        3. Это число делится на 31 без остатка?
#        4. Если это число больше 100 и оно делится на 17 без остатка или это число больше 150 и равно 13**2 тогда показать что это за число