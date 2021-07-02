# print(f'Создать предложение где одна его половина написана в маленьком регистре'.lower(), 'а вторая полностью в большом.'.upper())

# q = input('Введите текст : ')
# w = input('Введите текст : ')
# print(q.lower(), w.upper())


txt = 'Создать предложение где одна его половина написана в маленьком регистре, а вторая полностью в большом.'
txt1 = len(txt)
lower_case = txt.lower()
upper_case = txt.upper()
cut_len = txt1 - (txt1 // 2)
printlen = lower_case[: cut_len] + upper_case[cut_len :]
print(printlen)

# d = text.split(input('Создать предложение где одна его половина написана в маленьком регистре, а вторая полностью в большом.')
# r = len(d)
# for g in range(r // 2):
#     print(d[g].upper(), end='')
# s = r - r // 2
# while s < r:
#     print(d[s].lower(), end='')
#     s += 1





# 'Создать предложение где одна его половина написана в маленьком регистре, а вторая полностью в большом.'