class Road:


    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
        self.mass = 25
        self.thickness = 5

    def mass_a(self):
        result = self._length * self._width * self.mass * self.thickness
        return print(f"Масса асфальта\n {self._length} м * {self._width} м * {self.mass} кг * {self.thickness} см = ", result, "т")

a = Road(20, 5000)
a.mass_a()