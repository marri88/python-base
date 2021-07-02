menu = {'lagman': 120, 'plov': 120, 'borsh': 100}
menu['beshbarmak'] = 130
menu.update({'lagman': 130})
menu['lagman'] = 140
menu.pop('borsh')
print(menu)





# Из Dictionary №1:
# Добавьте в меню 
#  'besh_barmak' который стоит  130 сом.

# Оказалось лагман слишком дешевый. Обновите цену на 135

# Ваш повар отвратительно готовит борщ, поэтому хотите удалить это блюдо.
# Удалить borsh