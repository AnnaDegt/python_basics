from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

с = 1
for el in cycle("Aufgabe4"):
    if с > 8:
        break
    else:
        print(el)
        с += 1