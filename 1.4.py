n = int(input('Введите целое положительное число: '))
m = n % 10
while n > 0:
    if m > n % 10:
        m = m
    else: m = n % 10
    n = n // 10
print(m)