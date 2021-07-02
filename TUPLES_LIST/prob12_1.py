tuple1 =(1, 'as', 2, 'df', 1.6, True, 'io', 125, False, 5.2, 25, 'ghd', 'fkj', 65, 'hbd')
# print (tuple1[0:3])
# print (tuple1[3:6])
# print (tuple1[6:9])
# print (tuple1[9:12])
# print (tuple1[12:15])

# tuple2 = tuple(tuple1[x:x + 3]  
#       for x in range(0, len(tuple1), 3)) 
# print (str(tuple2))
  

for x in range (0, len(tuple1), 3):
	print(tuple1[x:x+3])

# print(tuple1[i])

# tuple1 = (1, 2, 3, 4, 8, 12, 3, 34, 
#              67, 45, 1, 1, 43, 65, 9) 

# tuple2 = tuple(tuple1[x:x + 3]  
#       for x in range(0, len(tuple1), 3)) 
  
# print (str(tuple2))







# Создать Tuple из 15 различных объектов.

# Разрезать Tuple
# на 5 строк по 3 объекта в строке.