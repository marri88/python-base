# Написать lambda которая получает сколько дней ПРОШЛО с нового года 
# как параметр и говорит пользователю сколько дней ОСТАЛОСЬ до нового года.

#ver1
b = (lambda c,n: n - c )(62,365)
print('До нового года осталось:',b)

#ver2
date = (lambda a, b, c: f"сколько прошло с нового года в днях {a - b}\nсколько осталось до нового года в днях {a-c}") (365, 303, 62)
print(date )


