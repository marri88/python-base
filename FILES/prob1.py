# -week_2:Работа С файлами-
##################################################################################
# first picture: prob №1
# С помощью Linux запишите в Файл все названия директорий из "/" - корневого каталога. 
# Если у вас Windows, сделайте тоже самое
# Только с помощью команды dir. В итоге у вас на рабочем столе должен появиться файл directories.txt. 
# Откройте этот файл с помощью Python и выведите на экран все директории из directories.txt.

# r = open('/home/aimira/Рабочий стол/directories.txt', 'w')
# direct1 = ('desktop, python, snap, видео, документы, музыка, загрузки, изображение, рабочий стол, шаблоны, общедоступные')
# r.write(direct1)
# r.close

r = open('/home/aimira/python/python3/week2files/directories.txt', 'w')
r.write('''Desktop/   python/   snap/   Видео/   
	Документы/   Загрузки/   Изображения/   Музыка/   
	Общедоступные/  'Рабочий стол'/   Шаблоны/''')
r.close()
with open('directories.txt', 'r') as file:
    file.read()