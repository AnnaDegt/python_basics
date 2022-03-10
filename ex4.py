x = int(input("Введите действительное положительное число: "))
y = int(input("Введите целое отрицательное число: "))
x_1 = x
y_1 = 2

def my_funk(x, y):
    global y_1, x_1
    while y_1 < y or y_1 == y:
        result = x_1 * x
        x = result
        y_1 += 1
    return result

print(my_funk(x, y))