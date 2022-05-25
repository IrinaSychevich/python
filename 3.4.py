def my_func1(): # 1 способ
    x = abs(float(input('Введите действительное положительное число: ')))
    y = abs(float(input('Введите целое отрицательное число: ')))
    y = int(0-y)
    return x**y
print(my_func1())

def my_func2(): # 2 способ
    x = abs(float(input('Введите действительное положительное число: ')))
    y = abs(float(input('Введите целое отрицательное число: ')))
    y = int(0-y)
    z = 0
    while y + z < 0:
        c = 1 / (x**(1 + z))
        z += 1
    return c
print(my_func2())