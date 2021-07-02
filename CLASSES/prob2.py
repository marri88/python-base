# Нужно создать класс который принимет данные в формате dict. Эти данные, вы сможете взять из Classroom Data #1.
# Вам нужно создать 6 методов класса:
# Получить все ключи в TUPLE.
# Получить все значения в TUPLE.
# Получить все ключи в LIST.
# Получить все значения в LIST.
# Получить все ключи в SET.
# Получить все значения в SET.

# Ниже когда вы будете передавать Словарь классу он и вызывать из него любой метод Вы должны получать соответсвенно нужные типы данных.
# Example: my_class = Parser("DICT") | my_class.get_keys_tuple()

colors = {
"black": {
"category": "hue",
"type": "primary",
"code": {
"rgba": [255,255,255,1],
"hex": "#000"
}
},
"white": {
"category": "value",
"code": {
"rgba": [0,0,0,1],
"hex": "#FFF"
}
},
"red": {
"category": "hue",
"type": "primary",
"code": {
"rgba": [255,0,0,1],
"hex": "#FF0"
}
},
"blue": {
"category": "hue",
"type": "primary",
"code": {
"rgba": [0,0,255,1],
"hex": "#00F"
}
},
"yellow": {
"category": "hue",
"type": "primary",
"code": {
"rgba": [255,255,0,1],
"hex": "#FF0"
}
},
"green": {
"category": "hue",
"type": "secondary",
"code": {
"rgba": [0,255,0,1],
"hex": "#0F0"
}
}
}

class Dict_key_values():
    def __init__(self, color):
        self.color = color

    def keys_tuple(self):
        a = (self.color).keys()
        f = []
        t = []
        for x in a:
            f.append(((self.color[x]).keys())) #colorkey1
        


        return f

d = Dict_key_values(colors)
print(d.keys_tuple())