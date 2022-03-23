
user_list = []
generator = [int(el) for el in input("Введите список чисел: ").split()]
for i in range(1, len(generator) -1):
    if generator[i] <= generator[i+1]:
        user_list.append(generator[i+1])

print(f" Старый список: {generator}" )
print(f" Старый список: {user_list}" )