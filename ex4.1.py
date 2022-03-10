x = int(input("Введите действительное положительное число: "))
y = int(input("Введите целое отрицательное число: "))


def my_funk(x, y):
    result = x**y
    return result

print(my_funk(x, y))