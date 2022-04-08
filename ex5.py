class Complex_number:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        sum_1 = self.num_1 + other.num_1
        sum_2 = self.num_2 + other.num_2
        return f'Сумма комплексных чисел {self.num_1}+{self.num_2}i и {other.num_1}+{other.num_2}i = {sum_1}+{sum_2}i'

    def __mul__(self, other):
        mul_1 = self.num_1 * other.num_1
        mul_2 = self.num_2 * other.num_2
        return f'Произведение комплексных чисел {self.num_1}+{self.num_2}i и {other.num_1}+{other.num_2}i= {mul_1}+{mul_2}i'



number_1 = Complex_number(1, 2)
number_2 = Complex_number(2, 3)
print(number_1 + number_2)
print(number_1 * number_2)