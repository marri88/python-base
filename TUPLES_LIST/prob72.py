# names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon', 
#  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon']
# i = 0
# while i != len(names):
#  	i += 1
#  	i = i % 2 == 0
# 	print(i)




names=['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon']
for i in range (len(names)):
  if i%2==0:
    print(names[i])


# Удалить из Листа №1 все чётные индексы до 10