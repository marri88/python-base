# Напишите функцию которая спрашивает у пользователя login и password. 
# Напишите декоратор который шифрует эти данные и возвращает вам зашифрованные данные. 
# (Можете воспользоваться функцией ord и char, можете загуглить...)

def dec_registr(func):
    a = input('login: ')
    b = input('password: ')
    func(a,b)

@dec_registr
def regisrt(a, b):
    i = 0
    for x in a:
        print(i + ord(x))
        break
    t = 0
    for y in b:
        print(t + ord(y))
        break

#ver1
# def p_l(l):
#     i = 0
#     for x in l():
#         i = i + ord(x)
#     print(i) 
# @p_l
# def l_p():
#     a = input('Напишите log и пароль: ')
#     return a


