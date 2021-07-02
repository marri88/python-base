farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
q = (set(farm_2).difference(farm_1))
print(q)


# farm_1 = {"dog", "cat", "mouse", "sheep"} 
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# print(len(farm_1), len(farm_2), farm_2-farm_1)

# В SET №3 из Google Colab найдите объекты которых нет SET №2

# # Множество № 2:
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# # Множество № 3:
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}

# list_1=["a", "b", "c", "d", "e"]
# list_2=["a", "f", "c", "m"]
# list=(set(list_2).difference(list_1))
# print(list)
# # ['m', 'f']