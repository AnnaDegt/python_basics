import json

f_obj = open("text_7.txt", "r", encoding='utf')
readlines = f_obj.readlines()

list_firm = []
result_list = []
count = 0
for el in readlines:
    el = el.split(" ")
    new_list = el[2:]
    list_firm.append(el[0])
    for i in new_list:
        i = int(i)
        result_list.append(i)

bad_firm = []
bad = []
list_profit = []
while result_list != []:
    for el in readlines:
        el = el.split(" ")
        firm = el[0]
        if result_list[0] >= result_list[1]:
            profit = result_list[0] - result_list[1]
            list_profit.append(profit)
            del result_list[:2]
            print(f"У компании {el[0]} есть прибыль {profit}")
        else:
            profit = result_list[0] - result_list[1]
            print(f"Компания {el[0]} потерпела убыток {profit}")
            bad.append(profit)
            bad_firm.append(el[0])
            del result_list[:2]

m_profit = sum(list_profit) / len(list_profit)
print(f"Соедняя прибыль компаний, которые получили прибыль равна {m_profit}")

result = []
i = 0
dict_profit_1 = {}
while i != len(list_profit):
    dict_profit_2 = {list_firm[i]: list_profit[i]}
    i += 1
    dict_profit_1.update(dict_profit_2)

i = 0
while i != len(bad):
    dict_profit_3 = {bad_firm[i]: bad[i]}
    i += 1
    dict_profit_1.update(dict_profit_3)

result.append(dict_profit_1)
dict_m_profit = {"average_profit": m_profit}
result.append(dict_m_profit)
print(result)

with open("text_7.json", "w") as write_f:
    json.dump(result, write_f)
