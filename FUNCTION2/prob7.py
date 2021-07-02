# Создайте функцию которая принмает тип данных dictionary, 
# но возвращает два Tuple в одном из них все ключи, в другом только значения.


def dict_div(**kwargs):
    print(tuple(kwargs.keys()))
    print(tuple(kwargs.values()))

dict_div(**{'sdll': 12, 'jdsjs': 14})