class OwnError(Exception):
    num_1 = int(input("Введите первое число: "))
    num_2 = int(input("Введите второе число: "))

    @staticmethod
    def null():
        try:
            return print(f'Все хорошо: {OwnError.num_1 / OwnError.num_2}')
        except:
            return print(f"Делить на ноль нельзя")

OwnError.null()


