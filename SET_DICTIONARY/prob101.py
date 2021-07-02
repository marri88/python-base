suitcase1 = set()
i = 0
while i < 5:
    i += 1
    x = input('Положите 5 вещей в чемодан: ',)
    suitcase1.add(x)
    list(set(suitcase1))
suitcase1.pop()
print(suitcase1)


# suitcase1 = []
# clothes = ['shirt','cap','t-shirt','boxes','glass']
# g = 'glass'
# suitcase1.extend (clothes)
# print (suitcase1)
# suitcase1.remove (g)
# print (suitcase1)



# Вы собираетесь на Иссык-Куль. Пока ваш чемодан пуст: 
# suitcase = [] 
# Однако он
# может вместить всего 5 вещей.
# Положите 5 вещей в чемодан.
# Вы передумали, и решили убрать последнюю вещь.