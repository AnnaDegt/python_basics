def number():
    while True:
        num_1 = int(input("Напишите любое число: "))
        num_2 = int(input("Напишите второе число: "))
        try:
            result = num_1 / num_2
            break
        except ZeroDivisionError:
            print("На ноль делить нельзя!")
    return result

print(number())