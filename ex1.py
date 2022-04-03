class Matrix:

    def __init__(self, num_1, num_2, num_3):
        print("Даны данные для матрицы: ")
        self.num_1 = num_1
        print(self.num_1)
        self.num_2 = num_2
        print(self.num_2)
        self.num_3 = num_3
        print(self.num_3)

    def   __str__(self):
        return f"Привычный вид матрицы: \n {'  '.join(str(i) for i in self.num_1)} \n {'  '.join(str(i) for i in self.num_2)} \n {'  '.join(str(i) for i in self.num_3)}"

    def __add__(self, other):
        result_1 = []
        list_1 = other.num_1
        list_2 = other.num_2
        list_3 = other.num_3
        el = 0
        for i in list_1:
            i = int(i)
            num = i + self.num_1[el]
            el += 1
            result_1.append(num)
        el = 0
        for i in list_2:
            num = i + self.num_2[el]
            el += 1
            result_1.append(num)
        el = 0
        for i in list_3:
            num = i + self.num_3[el]
            el += 1
            result_1.append(num)
        return f"Результат сложения: \n {'  '.join(str(i) for i in result_1[:3])} \n {'  '.join(str(i) for i in result_1[3:6])} \n {' '.join(str(i) for i in result_1[6:9])}"


matrix = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
matrix_2 = Matrix([1, 1, 1], [2, 2, 2], [3, 3, 3])
print(str(matrix))
print(matrix + matrix_2)