#Задание №3

f_obj = open("text_3.txt", "r", encoding="utf")
stroka = f_obj.read()
print("Данные о сотрудниках: \n ")
print(stroka)
f_obj.close()

f_obj = open("text_3.txt", "r", encoding="utf")
stroka = f_obj.readlines()
stroka = list(stroka)
print("\n")
count = 0
print(f'Сотрудники с зарплатой ниже ожидаемой:' )
for el in stroka:
    list_1 = el.split(" ")
    dict_1 = {list_1[0]: int(list_1[1])}
    for k, v in dict_1.items():
        sum = count + v
        count = sum
        if v <= 20000 :
            print(k)

print('\n')
result = sum / len(stroka)
print(f"Средняя величина доходов сотрудников равна {result}")

f_obj.close()