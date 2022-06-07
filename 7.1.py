class Matrix:
    def __init__(self,  *args):
        self.l = [*args]

    def __add__(self, other):
        y = []
        for i in range(0, len(self.l)):
            z = []
            for j in range(0, len(self.l[i])):
                z.append(str(self.l[i][j] + other.l[i][j]))
            z = '  '.join(z)
            z = z + '\n'
            y.append(z)
        y = ''.join(y)
        return y

    def __str__(self):
        self.d = []
        for i in range(0, len(self.l)):
            self.a = []
            for j in range(0, len(self.l[i])):
                el = str(self.l[i][j])
                self.a.append(el)
            self.a = '  '.join(self.a)
            self.a = self.a + '\n'
            self.d.append(self.a)
        self.d = ''.join(self.d)
        return f'{self.d}'

m1 = Matrix([5, 6, 4], [8, 2, 7], [2, 4, 1])
print(m1)
m2 = Matrix([3, 5, 6], [7, 1, 3], [5, 0, 9])
print(m2)

print(f'Сумма:\n{m1 + m2}')