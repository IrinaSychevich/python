def my_func():
    a = input('Введите символ или набор символов: ')
    b = input('Введите символ или набор символов: ')
    c = input('Введите символ или набор символов: ')
    l = (a + ' ' + b + ' ' + c)
    l2 = l.split(' ')
    x1 = max(l2)
    l2.remove(x1)
    x2 = max(l2)
    try:
        x1 = int(x1)
        x2 = int(x2)
        my_sum = sum([x1, x2])
        return my_sum
    except ValueError:
        my_sum = x1 + x2
        return my_sum
print(my_func())