def division():
    a = int(input('Введите первое число (делимое): '))
    b = int(input('Введите второе число (делитель): '))
    try:
        div = a / b
    except ZeroDivisionError:
        return
    return div
print(division())