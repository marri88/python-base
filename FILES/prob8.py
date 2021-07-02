# Возьмите текст #2 из Classroom и вставьте его в текстовый файл. 
# Возьмите данные из файла и сложите зарплату за Май, Июль, Сентябрь и Ноябрь и посчитайте среднее арифмитечское за эти месяца.
#2 Monthes:
# January       18000
# February      32641
# March          28300
# April             11200
# May              21100
# June            19000
# July              8000
# August         72000
# September  12300
# October       17000
# November   25000
# December   30000

f = open('/home/aimira/python/python3/week2files/zarplata.txt', 'r')
a = (f.read().split())
i = 0
for x in range(int(len(a))):
	if a[x] == "May" or a[x] == "July" or a[x] == "September" or a[x] == "November":
		i = i + int(a[x+1])
print(i)