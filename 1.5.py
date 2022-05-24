revenue = int(input('Внесите значение выручки, руб: '))
costs = int(input('Внесите значение издержек, руб: '))
result = revenue - costs
if result > 0:
    print(f'Фирма имеет прибыль) В количестве {result} руб')
    profitability = result / revenue * 100
    print(f'Рентабельность составила {"%.2f" % profitability} %')
    employees = int(input('Внесите значение выручки, руб: '))
    print(f'Удельная прибыль составила {result / employees} руб/чел')
else:
    print(f'Фирма несет убытки( В количестве {0 - result} руб')