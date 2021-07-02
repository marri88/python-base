#  Вам дан список имён names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", 
# "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"] 
# и вытащите 4 рандомных имени оттуда и сохраните в другой список.
import random 
# list1 = random.choice(["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", 
# "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"] )
# list2 = random.choice(["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", 
# "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"] )
# list3 = random.choice(["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", 
# "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"] )
# list4 = random.choice(["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", 
# "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"] )
# l = (list1, list2, list3, list4)
# print(l)

list1 = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", 
 "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
list2 = []
i = 0
random.choice(list1)
while i < 4:
	list2.append(random.choice(list1))
	i = i + 1
print (list2)