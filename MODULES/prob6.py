# Возьмите список имён из задания №2 и сформируйте 4 разные команды из всех участников.

list1 = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", 
 "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
for x in range (0, len(list1), 4):
	print(list1[x:x+4])
