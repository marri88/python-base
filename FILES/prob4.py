# -week_2:Работа С файлами-
#####################################################################################
 # first picture: prob №4

# Создайте текстовый файл python.txt и запишите в него текст 1 из Classroom:
# Затем, считайте его. Пробежитесь по всем его словам, и если слово содержит
# букву “t” или “T”, то запишите его в список t_words = [ ]. После окончания списка,
# выведите на экран все полученные слова. Подсказка: используйте for.

h = open('/home/aimira/python/python3/week2files/python.txt', 'r')
t_words = []
c = (h.read().split())
for x in c:
    if "t" in x:
        t_words.append(x)
    if "T" in x:
        t_words.append(x)
print(t_words)
h.close()


# t_words = list()
# T_words = list()
# for x in h.read(): 
# 	if 't' in x:
# 		t_words.append(x)
# print(t_words)
# for y in h.read():
# 	if 'T'in y:
# 		T_words.append(y)
# print(T_words)
# h.close()


