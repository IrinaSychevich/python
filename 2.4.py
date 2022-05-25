l1 = input('Напишите пару слов о себе: ')
l2 = list(l1.split())
for ind, el in enumerate(l2, 1):
    if len(el) > 10:
        print(ind, el[0:10])
    else:
        print(ind, el)