# Напишите функцию которая спрашивает у вас чтобы вы хотели заказать покушать и выпить. 
# А затем записывает это всё в файл на рабочем столе menu.txt

def order(a, b):
	q = open('order.txt', 'w')
	q.write(f'{a}, {b}')
a =  input('покушать: ')
b =  input('выпить: ')
order(a, b)







