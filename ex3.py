import math

class Cell():

    def __init__(self, num_1):
        self.num_1 = num_1

    def __add__(self, other):
        #увеличение
        result_1 = self.num_1 + other.num_1
        return f'Результат сложения двух клеток: {result_1}'

    def __sub__(self, other):
        #уменьшение
        result_2 = self.num_1 - other.num_1
        if result_2 >= 0:
            return f'Результат вычитания двух клеток: {result_2}'
        else:
            return f'Результат отрицательный'

    def __mul__(self, other):
        #умножение
        result_3 = self.num_1 * other.num_1
        return f'Результат умножения двух клеток: {result_3}'

    def __floordiv__(self, other):
        #целочисленное деление без остатка
        self.result_4 = self.num_1 // other.num_1
        return f'Результат деления двух клеток: {self.result_4}'

    def make_order(self, num_2):
        #ячейки по рядам
        self.num_2 = num_2
        list = []
        list_1 = []
        for i in range(self.num_1):
            i += 1
            list.append(i)
        answer = self.num_1 / self.num_2
        for el in range(math.ceil(answer)):
            list_1.append(list[ : self.num_2])
            for i in list_1:
                print('*' * len(i))
            del list_1[:]
            del list[:self.num_2]





c = Cell(12)
b = Cell(8)
print(c + b)
print(c - b)
print(c * b)
print(c // b)
c.make_order(5)
