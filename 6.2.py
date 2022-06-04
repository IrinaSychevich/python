class Road():
    thickness = 0.05
    specific_weight = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self):
        weight = self._length * self._width * Road.thickness * Road.specific_weight
        return weight

a = Road(20, 5000)
print(a.weight())
