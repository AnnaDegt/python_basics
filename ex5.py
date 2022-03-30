class Stationery:

    title = 'Канцелярия'

    def draw(self):
        return print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        return print("Я рисую ручкой")

class Pencil(Stationery):
    def draw(self):
        return print("Я рисую карандашом")

class Handle(Stationery):
    def draw(self):
        return print("Я рисую маркером")

s = Stationery()
print(s.title)
s.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()