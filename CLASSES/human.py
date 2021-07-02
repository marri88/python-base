class Human:
    #Статические поля
    default_name = 'No name'
    default_age = 0

    def __init__(self, name=default_name, age=default_name):
        #Динамические поля
        #Публичные
        self.name = name
        self.age = age
        #Приватные
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Money: {self.__money}')
        print(f'House: {self.__house}')

    # Статический метод
    @staticmethod
    def default_info():
        print(f'Default Name: {Human.default_name}')
        print(f'Default Age: {Human.default_age}')

    def earn_money(self, amount):
        self.__money += amount
        print(f'Earned {amount} moneu! Current value: {self.__money}')

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print('Not enough money!')


    # Приватный метод
    def __make_deal(self, house, price):
        self.__money = price
        self.__house = house


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f'Final price: {final_price}')
        return final_price

class SmallHouse(House):

    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)

if __name__ == '__main__':
    print(Human.default_name)

    # fedor = Human('Fedor', 32)
    #
    # fedor.info()
    # Human.default_info()
    #
    # fedor.earn_money(10000)
    # fedor.info()
    #
    # house = House(100, 15000)
    # fedor.buy_house(house, 3)

    Human.default_info()
    alex = Human('Alex', 20)
    alex.info()

    small_house = SmallHouse(8500)
    alex.buy_house(small_house, 5)

    alex.earn_money(5000)
    alex.buy_house(small_house, 5)


    alex.earn_money(20000)
    alex.buy_house(small_house, 5)
    alex.info()


