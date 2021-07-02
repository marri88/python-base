lang1 = "Rust"
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby', 'Rust']
for i in range(6):
# for i in languages:
# 	if lang1 in i:
# 		print('yes')
	if languages[i] == lang1:
			print ("yes")
	else:
		print("no")

# 1. Допустим у нас есть список языков программирования.
#   lang1 = 'Rust'
#   languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
#   Обязательное условие: если переменная в списке, то нужно вывеvсти на экран 'this languages is in list'. 
#   Если этого языка нет в
#   списке, ничего не нужно выводить.