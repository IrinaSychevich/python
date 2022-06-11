from math import fabs
class ComplexNumber:
    def __init__(self, real_number, imaginary_number):
        self.real_number = real_number
        self.imaginary_number = imaginary_number

    def parts_of_number(self):
        try:
            self.real_number = int(self.real_number)
        except ValueError:
            return 'Вы неправильно ввели действительную часть комплексного числа!'
        self.imaginary_number = self.imaginary_number.replace('i', '')
        try:
            self.imaginary_number = int(self.imaginary_number)
        except ValueError:
            return 'Вы неправильно ввели мнимую часть комплексного числа!'
        return self.real_number, self.imaginary_number

    def __add__(self, other):
        return ComplexNumber(int(self.real_number) + int(other.real_number), int(self.imaginary_number) + int(other.imaginary_number))

    def __mul__(self, other):
        a = (int(self.real_number) * int(other.real_number))
        b = (int(self.imaginary_number) * int(other.imaginary_number))
        b = -b
        c = (int(self.real_number) * int(other.imaginary_number))
        d = (int(self.imaginary_number) * int(other.real_number))
        mul_real_number = a + b
        mul_imaginary_number = c + d
        return ComplexNumber(mul_real_number, mul_imaginary_number)

    def __str__(self):
        if self.imaginary_number < 0:
            return f'{self.real_number} - {int(fabs(self.imaginary_number))}i'
        else:
            return f'{self.real_number} + {self.imaginary_number}i'


a1 = input('Введите действительную часть комплексного числа: ')
b1 = input('Введите мнимую часть комплексного числа: ')
g1 = ComplexNumber(a1, b1)


a2 = input('Введите действительную часть комплексного числа: ')
b2 = input('Введите мнимую часть комплексного числа: ')
g2 = ComplexNumber(a2, b2)


a3 = input('Введите действительную часть комплексного числа: ')
b3 = input('Введите мнимую часть комплексного числа: ')
g3 = ComplexNumber(a3, b3)


v = g1 + g2 + g3
print(f'Сумма: {v}')

h = g1 * g2 * g3
print(f'Произведение: {h}')