f_obj = open("text_6.txt", "r", encoding='utf')
list_1 = f_obj.readlines()

dict = {}
list_number = []
for el in list_1:
    el = el.split(' ')
    list_number.append(el[1:])

i = 0
new_list = []

count_2 = 0
list = []
for element in list_number:
    for number in element:
        sum_number = len(element)
        i = 0
        count_1 = 0
        while True:
                # count_1 != len(element):
              if number[i] != "(":
                i += 1
                count_1 += 1
              else:
                  new_number = number[:i]
                  new_list.append(int(new_number))
                  break
    list.append(sum_number)

new_new_list = []
for m in list:
    new_new_list.append(sum(new_list[:m]))
    del new_list[:m]

v = 0
for el in list_1:
    el = el.split(' ')
    dict[el[0]] = new_new_list[v]
    v += 1

print(dict)
f_obj.close()