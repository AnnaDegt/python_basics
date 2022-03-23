#a - выработка в час
#b - ставка в час
#c - премия

from sys import argv

# #первый вариант через Pycharm
work = int(input("Введите выработку в час: "))
st = int(input("Введите ставку в час: "))
pr = int(input("Введите размер премии: "))

def payment(a, b, c):
    result = (a * b) + c
    return result

print(payment(work, st, pr))

#второй вариант через PowerShell
name_1, a, b, c = argv
result = (int(a) * int(b)) + int(c)

print(result)