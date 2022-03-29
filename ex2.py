# Задание №2

f_obj = open("text_2.txt", 'r')
text_1 = f_obj.read()
print(text_1)
f_obj.close()
f_obj = open("text_2.txt", 'r')
text = f_obj.readlines()
st_count = len(text)
print(f"Это содержимое файла: \n ")


user_list = []

print(f"Всего {st_count} строк")

for el in text:
    new_list = el.split(" ")
    word_count = len(new_list)
    user_list.append(word_count)

for i in range(st_count):
    print(f"На {i + 1} - ой строке ровно {user_list[i]} слов(a)")

f_obj.close()