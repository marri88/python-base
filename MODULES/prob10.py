# Создайте игру Камень-Ножницы-Бумага с Компьютером. 
# Где компьютер даёт вам выбрать опцию, а сам затем генерирует своё значение. 
# По итогу говорит выиграли вы, проиграли или ничья.


a = [0]*4 
import random
for i in range (4):
    ver = 0
    while (ver==0):
        player = int(input("1 - камень, 2 - ножницы, 3 - бумага. "))
        if (player == 1 or player == 2 or player == 3):
            ver = 1
    a[i] = player     
    if player == 1:
        print("Вы выбрали камень.")
    if player == 2:
        print("Вы выбрали ножницы.")
    if player == 3:
        print("Вы выбрали бумагу.")
    comp = random.randint(1,3)
    if comp == 1:
        print("Компьютер выбрал камень.")
    if comp == 2:
        print("Компьютер выбрал ножницы.")
    if comp == 3:
        print("Компьютер выбрал бумагу.")
    # определяем победителя
    if player == comp:
        win = 0
    if player == 1 and comp == 2:
        win = 1 
    if player == 1 and comp == 3:
        win = 2
    if player == 2 and comp == 1:
        win = 2
    if player == 2 and comp == 3:
        win = 1
    if player == 3 and comp == 1:
        win = 1
    if player == 3 and comp == 2:
        win = 2
    if win == 0:
        print("Ничья!")
    if win == 1:
        print("Победил игрок!")
    if win == 2:
        print("Победил компьютер!")
print (a)
k = 0
n = 0
b = 0
for i in range (4):
    if a[i] == 1:
        k = k+1
    if a[i] == 2:
        n = n+1
    if a[i] == 3:
        b = b+1
ver = 0
comp = 1
if k>2:
    comp=3
if n>2:
    comp = 1
if b>2:
    comp = 2
    
while (ver==0):
    player = int(input("1 - камень, 2 - ножницы, 3 - бумага. "))
    if (player == 1 or player == 2 or player == 3):
        ver = 1
if player == 1:
        print("Вы выбрали камень.")
if player == 2:
        print("Вы выбрали ножницы.")
if player == 3:
        print("Вы выбрали бумагу.")
if comp == 1:
        print("Компьютер выбрал камень.")
if comp == 2:
        print("Компьютер выбрал ножницы.")
if comp == 3:
        print("Компьютер выбрал бумагу.")
    # определяем победителя
if player == comp:
        win = 0
if player == 1 and comp == 2:
        win = 1 
if player == 1 and comp == 3:
        win = 2
if player == 2 and comp == 1:
        win = 2
if player == 2 and comp == 3:
        win = 1
if player == 3 and comp == 1:
        win = 1
if player == 3 and comp == 2:
        win = 2
if win == 0:
        print("Ничья!")
if win == 1:
        print("Победил игрок!")
if win == 2:
        print("Победил компьютер!")


# import random
 
# print("---Game---")
# print("Stone/Scissors/Paper")
# app = random.randint(1, 3)
# if app == 1:
#     gg = "Stone"
# elif app == 2:
#     gg = "Scissors"
# else:
#     gg = "Paper"
# print("1)Stone")
# print("2)Scissors")
# print("3)Paper")
# try:
#     x = int(input("Write the number:/n> "))
#     if x == 1:
#         print("")
#         print("Your choise: Stone")
#         print("Opponent choise: " + str(gg))
#         print("")
#         if app == 1:
#             print("Draw :/")
#         elif app == 2:
#             print("You win! :3")
#         else:
#             print("Opponent win\n Your Lose! :c")
#             print("")
#     elif x == 2:
#         print("")
#         print("Your choise: Scissors")
#         print("Opponent choise: " + str(gg))
#         print("")
#         if app == 1:
#             print("Opponent win\n Your Lose! :c")
#         elif app == 2:
#             print("Draw :/")
#         else:
#             print("You win! :3")
#             print("")
#     elif x == 3:
#         print("")
#         print("Your choise: Paper")
#         print("Opponent choise " + str(gg))
#         print("")
#         if app == 1:
#             print("You win! :3")
#         elif app == 2:
#             print("Opponent win\n Your Lose! :c")
#         else:
#             print("Draw :/")
#         print("")
#     else:
#         print("Write only numbers: 1/2/3!")
# except ValueError:
#     print("ERROR: Write only INT numbers!")



# import random
 
# print("---Game---")
# print("Stone/Scissors/Paper")
# app = random.randint(1, 3)
# if app == 1:
#     gg = "Stone"
# elif app == 2:
#     gg = "Scissors"
# else:
#     gg = "Paper"
# print("1)Stone")
# print("2)Scissors")
# print("3)Paper")
# try:
#     x = int(input("Write the number:/n> "))
#     if x == 1:
#         print("")
#         print("Your choise: Stone")
#         print("Opponent choise: " + str(gg))
#         print("")
#         if app == 1:
#             print("Draw :/")
#         elif app == 2:
#             print("You win! :3")
#         else:
#             print("Opponent win\n Your Lose! :c")
#             print("")
#     elif x == 2:
#         print("")
#         print("Your choise: Scissors")
#         print("Opponent choise: " + str(gg))
#         print("")
#         if app == 1:
#             print("Opponent win\n Your Lose! :c")
#         elif app == 2:
#             print("Draw :/")
#         else:
#             print("You win! :3")
#             print("")
#     elif x == 3:
#         print("")
#         print("Your choise: Paper")
#         print("Opponent choise " + str(gg))
#         print("")
#         if app == 1:
#             print("You win! :3")
#         elif app == 2:
#             print("Opponent win\n Your Lose! :c")
#         else:
#             print("Draw :/")
#         print("")
#     else:
#         print("Write only numbers: 1/2/3!")
# except ValueError:
#     print("ERROR: Write only INT numbers!")





# import random
 
# print("---Game---")
# print("Stone/Scissors/Paper")
# app = random.randint(1, 3)
# if app == 1:
#     gg = "Stone"
# elif app == 2:
#     gg = "Scissors"
# else:
#     gg = "Paper"
# print("1)Stone")
# print("2)Scissors")
# print("3)Paper")
# try:
#     x = int(input("Write the number:/n> "))
#     if x == 1:
#         print("")
#         print("Your choise: Stone")
#         print("Opponent choise: " + str(gg))
#         print("")
#         if app == 1:
#             print("Draw :/")
#         elif app == 2:
#             print("You win! :3")
#         else:
#             print("Opponent win\n Your Lose! :c")
#             print("")
#     elif x == 2:
#         print("")
#         print("Your choise: Scissors")
#         print("Opponent choise: " + str(gg))
#         print("")
#         if app == 1:
#             print("Opponent win\n Your Lose! :c")
#         elif app == 2:
#             print("Draw :/")
#         else:
#             print("You win! :3")
#             print("")
#     elif x == 3:
#         print("")
#         print("Your choise: Paper")
#         print("Opponent choise " + str(gg))
#         print("")
#         if app == 1:
#             print("You win! :3")
#         elif app == 2:
#             print("Opponent win\n Your Lose! :c")
#         else:
#             print("Draw :/")
#         print("")
#     else:
#         print("Write only numbers: 1/2/3!")
# except ValueError:
#     print("ERROR: Write only INT numbers!")




# import random
 
# print("---Game---")
# print("Stone/Scissors/Paper")
# app = random.randint(1, 3)
# if app == 1:
#     gg = "Stone"
# elif app == 2:
#     gg = "Scissors"
# else:
#     gg = "Paper"
# print("1)Stone")
# print("2)Scissors")
# print("3)Paper")
# try:
#     x = int(input("Write the number:/n> "))
#     if x == 1:
#         print("")
#         print("Your choise: Stone")
#         print("Opponent choise: " + str(gg))
#         print("")
#         if app == 1:
#             print("Draw :/")
#         elif app == 2:
#             print("You win! :3")
#         else:
#             print("Opponent win\n Your Lose! :c")
#             print("")
#     elif x == 2:
#         print("")
#         print("Your choise: Scissors")
#         print("Opponent choise: " + str(gg))
#         print("")
#         if app == 1:
#             print("Opponent win\n Your Lose! :c")
#         elif app == 2:
#             print("Draw :/")
#         else:
#             print("You win! :3")
#             print("")
#     elif x == 3:
#         print("")
#         print("Your choise: Paper")
#         print("Opponent choise " + str(gg))
#         print("")
#         if app == 1:
#             print("You win! :3")
#         elif app == 2:
#             print("Opponent win\n Your Lose! :c")
#         else:
#             print("Draw :/")
#         print("")
#     else:
#         print("Write only numbers: 1/2/3!")
# except ValueError:
#     print("ERROR: Write only INT numbers!")

