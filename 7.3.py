class Cell:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return Cell(self.n + other.n)

    def __sub__(self, other):
        Cell(self.n - other.n)
        if (self.n - other.n) > 0:
            return Cell(self.n - other.n)
        else:
            return 'Разница отрицательная'

    def __mul__(self, other):
        return Cell(self.n * other.n)

    def __truediv__(self, other):
        return Cell(int(self.n / other.n))

    @property
    def make_order(self):
        a = int(self.n / 5)
        b = self.n % 5
        t = []
        w = '*****\n'
        q = '*'
        while a > 0:
            t.append(w)
            a -=1
        while b > 0:
            t.append(q)
            b -= 1
        t = ''.join(t)
        return t

    def __str__(self):
        return f'Результат математической операции: {self.n}'

c1 = Cell(29)
c2 = Cell(15)
c3 = Cell(8)
print(c1.make_order)
print(c2.make_order)
print(c3.make_order)
print(c1 + c2 + c3)
try:
    print(c1 - c2 - c3)
except TypeError:
    print('Разница отрицательная')
print(c1 * c2 * c3)
print(c1 / c2 / c3)

