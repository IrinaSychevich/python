l1 = input('Введите элементы списка через пробел: ')
l2 = list(l1.split())
m = 0
while m <= len(l2) - 2:
    l2[m], l2[m + 1] = l2[m + 1], l2[m]
    m = m + 2
print(l2)
