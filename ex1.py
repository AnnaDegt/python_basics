class Date:

    def __init__(self, string):
        self.user_date = string

    @classmethod
    def number(cls, obj):
        obj.user_date = obj.user_date.split('-')
        for el in range(2):
            obj.user_date[el] = int(obj.user_date[el])
        return print(obj.user_date[0], obj.user_date[1], obj.user_date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31 and 1 <= month <= 12 and year <= 2023:
            return print(f'Все хорошо, ваша дата: {day} {month} {year}')
        else:
            return print("Пересмотрите дату")


d = Date('11-10-2001')
Date.number(d)
Date.valid(11,10,2001)