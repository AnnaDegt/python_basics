from math import factorial

def fact(n):
    for i in range(n):
        print(f"{i}! = ", end = "")
        yield factorial(i)

for el in fact(15):
    print(el)

