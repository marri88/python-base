# Через Python у себя на рабочем столе создайте директорию, а внутри дериктории создайте 5 РАНДОМНЫХ файлов.\

import os
import random
os.mkdir("week2modules2prob5")

i = 0
while i < 5:
	a = random.randint(1, 100)
	os.mknod(f'/home/aimira/python/python3/week2modules/week2modules2prob5/1{a}.txt')
	i += 1
print(i)

# os.mknod('/home/aimira/python/python3/week2modules/week2modules2prob5/1.txt')
# os.mknod('/home/aimira/python/python3/week2modules/week2modules2prob5/2.txt')
# os.mknod('/home/aimira/python/python3/week2modules/week2modules2prob5/3.txt')
# os.mknod('/home/aimira/python/python3/week2modules/week2modules2prob5/4.txt')
# os.mknod('/home/aimira/python/python3/week2modules/week2modules2prob5/5.txt')

