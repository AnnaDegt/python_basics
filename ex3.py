class Worker( ):

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
        self.wage = self._income["wage"]
        self.bonus = self._income["bonus"]

class Position(Worker):
    def get_full_name(self):
        return print(f'Уважаемый сотрудник, {self.name} {self.surname}')

    def get_total_income(self):
        result = self._income["wage"] + self._income["bonus"]
        return print(f'Ваш доход равен {result}')

a = Position("Петр", "Петров", "завхоз", 10000, 3000)
a.get_full_name()
a.get_total_income()