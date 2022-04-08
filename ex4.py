#класс склад
class Stock:
    #place - место на складе для конкретной техники
    place_printer = 10
    place_scanner = 15
    place_xerox = 12

#класс оргтехника
class Office_equipment:
    class_IT = [2, 4, 5]
    class_develop = [4, 5, 2]
    class_analytics = [3, 5, 1]

    list_printer = []
    new_list_printer = []
    list_scanner = []
    new_list_scanner = []
    list_xerox = []
    new_list_xerox = []
    def __init__(self, place, type_obj):
        #place - организация
        self.place = place
        #type_obj - техника
        self.type_obj = type_obj




class Printer(Office_equipment):
    def __init__(self, number, year, color):
        self.number = number
        self.year = year
        self.color = color



    def stock_printer(self):
        try:
            if self.number <= Stock.place_printer:
                dict_printer = {"Количество принтеров": self.number}
                free_place = Stock.place_printer - self.number
                print(f'Прием одобрен. Информация о товаре: {dict_printer}. Пустое место на складе: {free_place}')
                if self.number >= Office_equipment.class_IT[0]:
                    self.number -= Office_equipment.class_IT[0]
                    print("Принтеры направлены компании IT")
                    if self.number >= Office_equipment.class_develop[0]:
                        self.number -= Office_equipment.class_develop[0]
                        print("Принтеры направлены компании разработчиков")
                        if self.number >= Office_equipment.class_analytics[0]:
                            self.number -= Office_equipment.class_analytics[0]
                            print('Принтеры направлены компании аналитиков')
                        else:
                            print('Принтеров хватило только для первых двух компаний')
                    else:
                        print('Принтеров хватило только для первой компании')
                else:
                    print("Принтеров не хватает даже для первой компании IT")
            else:
                print("Прием отклонен. Склад для принтеров заполнен")
        except TypeError:
            print('Проверьте корректность данных для принтеров')
        except ValueError:
            print('Проверьте корректность данных для ксероксов')
        except NameError:
            print('Проверьте корректность данных для принтеров')

    def valid(self):
        try:
            self.year + self.number
        except:
                print("Проверьте или уточните данные количества и года для принтеров")
        else:
                print("Все данные корректны для приннтеров")

class Scanner(Office_equipment):
    def __init__(self, number, year, color):
        self.number = number
        self.year = year
        self.color = color


    def stock_scanner(self):
        try:
            if self.number <= Stock.place_scanner:
                dict_scanner = {"Количество сканеров": self.number}
                free_place = Stock.place_scanner - self.number
                print(f'Прием одобрен. Информация о товаре: {dict_scanner}. Пустое место на складе: {free_place}')
                if self.number >= Office_equipment.class_IT[1]:
                    self.number -= Office_equipment.class_IT[1]
                    print("Сканеры направлены компании IT")
                    if self.number >= Office_equipment.class_develop[1]:
                        self.number -= Office_equipment.class_develop[1]
                        print("Сканеры направлены компании разработчиков")
                        if self.number >= Office_equipment.class_analytics[1]:
                            self.number -= Office_equipment.class_analytics[1]
                            print('Сканеры направлены компании аналитиков')
                        else:
                            print('Сканеров хватило только для первых двух компаний')
                    else:
                        print('Сканеров хватило только для первой компании')
                else:
                    print("Сканеров не хватает даже для первой компании IT")
            else:
                print("Прием отклонен. Склад для сканеров заполнен")
        except TypeError:
            print('Проверьте корректность данных для сканеров')
        except ValueError:
            print('Проверьте корректность данных для ксероксов')
        except NameError:
            print('Проверьте корректность данных для сканеров')

    def valid(self):
        try:
            self.year + self.number
        except:
                print("Проверьте или уточните данные количества и года для сканеров")
        else:
                print("Все данные корректны для сканеров")

class Xerox(Office_equipment):
    def __init__(self, number, year, color):
        self.number = number
        self.year = year
        self.color = color

    def stock_xerox(self):
        try:
            if self.number <= Stock.place_xerox:
                dict_xerox = {"Количество ксероксов": self.number}
                free_place = Stock.place_xerox - self.number
                print(f'Прием одобрен. Информация о товаре: {dict_xerox}. Пустое место на складе: {free_place}')
                if self.number >= Office_equipment.class_IT[2]:
                    self.number -= Office_equipment.class_IT[2]
                    print("Ксероксы направлены компании IT")
                    if self.number >= Office_equipment.class_develop[2]:
                        self.number -= Office_equipment.class_develop[2]
                        print("Ксероксы направлены компании разработчиков")
                        if self.number >= Office_equipment.class_analytics[2]:
                            self.number -= Office_equipment.class_analytics[2]
                            print('Ксероксы направлены компании аналитиков')
                        else:
                            print('Ксероксов хватило только для первых двух компаний')
                    else:
                        print('Ксероксов хватило только для первой компании')
                else:
                    print("Ксероксов не хватает даже для первой компании IT")
            else:
                print("Прием отклонен. Склад для ксероксов заполнен")
        except TypeError:
            print('Проверьте корректность данных для ксероксов')
        except ValueError:
            print('Проверьте корректность данных для ксероксов')
        except NameError:
            print('Проверьте корректность данных для ксероксов')

    def valid(self):
        try:
            self.year + self.number
        except:
                print("Проверьте или уточните данные количества и года для ксероксов")
        else:
                print("Все данные корректны для ксероксов")

printer = Printer(5, " ", True)
scanner = Scanner(8, 2005, False)
xerox = Xerox(' ', 2017, True)


printer.stock_printer()
scanner.stock_scanner()
xerox.stock_xerox()
printer.valid()
scanner.valid()
xerox.valid()


