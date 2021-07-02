farm2 = {"dog", "cat", "mouse", "sheep"}
farm3 = {"cow", "horse", "donkey", "cat", "dog"}
farm1 = set.union(farm2, farm3)
print(farm1)

farm2 = {"dog", "cat", "mouse", "sheep"}
farm3 = {"cow", "horse", "donkey", "cat", "dog"}
farm4 = (set(farm3).difference(farm2))
print(farm4)



# Из Google Colab Множество 2 и 3 
# Напишите код, который: Выведет новое множество, которое есть как в
# первой ферме, так и во второй.

# Выведет новое МНОЖЕСТВО, состоящее из животных,
# которые есть в первой ферме, но нет во второй.

# # Множество № 2:
# farm_1 = {"dog", "cat", "mouse", "sheep"}
 
# # Множество № 3:
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
