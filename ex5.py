def my_summa():
    summa = 0
    while True:
        list = 0
        user_number = input("Введите числа через пробел, для выхода последним числом введите '#'").split()
        cont = 0
        if user_number[-1] == "#":
            del user_number[-1]
            while cont < len(user_number):
                list= list + int(user_number[cont])
                cont += 1
            summa = summa + list
            print(summa)
            break

        while cont < len(user_number):
            list= list + int(user_number[cont])
            cont += 1

        summa = summa + list
        print(summa)

my_summa()

