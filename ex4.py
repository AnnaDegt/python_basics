f_obj = open("text_4.txt", "r", encoding='utf')
text_1 = f_obj.readlines()

dict = {'One':'Один', 'Two': 'Два', 'Three': 'Три', 'Four' : 'Четыре'}
i = 1
for el in text_1:
    el = el.split(' — ')
    for k, v in dict.items():
        if el[0] == k :
            print(f'{v} — {i}')
            i += 1

f_obj.close()