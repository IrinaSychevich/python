from abc import ABC, abstractmethod
class Сlothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Сlothes):
    def __init__(self, size):
        self.v = size

    @property
    def consumption(self):
        self.c_cloth = self.v / 6.5 + 0.5
        return self.c_cloth


class Suit(Сlothes):
    def __init__(self, height):
        self.h = height

    @property
    def consumption(self):
        self.s_cloth = 2 * self.h + 0.3
        return self.s_cloth


c = Coat(42)
print(c.consumption)
s = Suit(120)
print(s.consumption)
g = print(c.consumption + s.consumption)
