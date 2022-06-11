class Division:
    def __init__(self, divisible, divider):
        self.divisible = divisible
        self.divider = divider

    @classmethod
    def new_format_numbers(cls, numbers):
        numbers_list = numbers.split(',')
        divisible, divider = numbers_list
        divisible = int(divisible)
        divider = int(divider)
        return cls(divisible, divider)

x = input('Введите делимое и делитель через запятую: ')
numbers = Division.new_format_numbers(x)
divisible = numbers.divisible
divider = numbers.divider

class DivisionZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt

try:
    if divider == 0:
        raise DivisionZeroError("Вы ввели в качестве делителя 0. На ноль делить нельзя!")
except DivisionZeroError as err:
    print(err)
else:
    division = divisible / divider
    print(f"Все хорошо. Ваше число: {division}")




