class Car:

    def __init__(self, name, speed, color, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Машина едет'

    def stop(self):
        return 'Машина остановилась'

    def turn(self, direction):
        return f'Машина повернула {direction}'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.speed}'

class TownCar(Car):
    def show_speed(self):
        if self.speed >= 60:
            return 'Превышение скорости для TownCar'
        else:
            return 'Скорость нормальная'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 40:
            return 'Превышение скорости для WorkCar'
        else:
            return 'Скорость нормальная'

class PoliceCar(Car):
    pass


town = TownCar('Nissan', 100, 'grey', False)
print(f"1:{town.go()}, {town.show_speed()}, {town.turn('left')}, {town.stop()}")
work = WorkCar("WAZ", 50, 'white', False)
print(f'2:{work.go()}, {work.show_speed()}, {work.turn("left")}, {work.stop()} ' )
sport = SportCar('GT40', 200, 'black', False)
print(f'3:{sport.go()}, {sport.show_speed()}, {sport.turn("right")}, {sport.stop()} ')
police = PoliceCar('Ford', 40, 'blue', True)
print(f'4:{work.go()}, {work.show_speed()}, {work.turn("right")}, {work.stop()}')

print('Примеры вывода атрибутов:')
print(town.speed)
print(work.color)
print(sport.name)
print(police.is_police)
