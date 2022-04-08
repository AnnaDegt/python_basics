class OwnError(Exception):

    @staticmethod
    def numbers():
        new_list = []
        while True:
            try:
                list_num = int(input('Введите число: '))
                new_list.append(list_num)
                print (f'Текущий список - {new_list} \n ')
                try_1 = input('Хотите еще раз попробовать? try or stop?: ')
                if try_1 == 'stop':
                    print(f'Ладно, итоговый список: {new_list}')
                    break
            except:
                print(f"Есть недопустимое значение - строка и булево")
                try_1 = input('Хотите еще раз попробовать? try or stop?: ')
                if try_1 == 'stop':
                    print(f'Ладно, итоговый список: {new_list}')
                    break


OwnError.numbers()