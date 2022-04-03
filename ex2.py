from abc import ABC, abstractmethod

class Clothes(ABC):
    Coat = "Пальто"
    Costume = "Костюм"

    def __init__(self, size):
        self.size = size

    @abstractmethod
    def result(self):
        return 'Это обязательный метод'

class Coat(Clothes):

    def result(self):
        return f'Расход ткани на {Clothes.Coat} :  {self.size / 6.5 + 0.5}'

class Costume(Clothes):

    def result(self):
        return f'Расход ткани на {Clothes.Costume} :  {2 * self.size + 0.3}'

    @property
    def total(self):
        answer = (self.size / 6.5 + 0.5) + (2 * self.size + 0.3)
        return f"Всего нам потребуется {answer} ткани"


c = Coat(6.5)
b = Costume(2)
print(b.total)
