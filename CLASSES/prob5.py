# Создайте Класс Zoo.
# Инициализируйте класс в объект.
# К объекту Zoo добавьте атрибут animal_1 и присвойте ему значение "Тигр"
# К объекту Zoo добавьте атрибут animal_2 и присвойте ему значение "Бегемот"
# К объекту Zoo добавьте атрибут animal_3 и присвойте ему значение "Жираф"
# В объекте Zoo измените значение атрибута animal_1 и присвойте ему значение "Лев".
# К объекту Zoo добавьте атрибут animal_4 и присвойте ему list состоящий из animal_2 и animal_3
# В объекте Zoo измените значение атрибута animal_3 и присвойте ему значение "Змея"

class Zoo:
    def __init__(self):
        self.animal_1 = 'Tiger'
        self.animal_2 = 'Begemot'
        self.animal_3 = 'Jiraf'
        
z = Zoo()

z.animal_1 = 'Lion'
z.animal_4 = [z.animal_2, z.animal_3]
z.animal_3 = 'Snake'

print(z.animal_1)
print(z.animal_2)
print(z.animal_3)
print(z.animal_4)
