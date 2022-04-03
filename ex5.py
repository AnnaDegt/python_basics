f_obj = open("text_5.txt", "w")
user_number = input("Запишите набор чисел через пробел: ")
f_obj.write(user_number)
user_number_list = list(user_number.split(' '))

count = 0
for el in user_number_list:
    sum = count + int(el)
    count = sum

print(f'Сумма введенных чисел равна {sum}')

f_obj.close()