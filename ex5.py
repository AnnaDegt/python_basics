

def sum_user():
    summa = 0
    while True:
        list_user = input("Введите cтроку чисел через пробел: ")
        result = list_user.split()
        result_user = ("".join(map(str, result)))
        for el in result:
            if el == "#":
                print("Выполнение кода завершено")
                break
            break
        for el in result:
            number = [int(i) for i in str(result_user)]
            for element in number:
                summa += element

    return summa

print(sum_user())