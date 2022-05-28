from math import factorial
n = int(input('Введите число: '))
my_list = list(range(1, n+1))
def fact():
    for el in my_list:
        factor = factorial(el)
        yield factor
n = 1
for el in fact():
    print(f'факториал {n} равен {el}')
    n +=1
