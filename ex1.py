# Задание №1

f_obj = open("text.txt", "w")
user_date = input("Введите текстовые данные: ")
while user_date != " ":
    f_obj.writelines(user_date)
    user_date = input("Введите текстовые данные: ")

f_obj.close()
f_obj = open("text.txt", "r")
date = f_obj.readlines()
print('Завершение работы программы')
f_obj.close