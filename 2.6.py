k = 1
d = []
m1 = []
p1 = []
n1 = []
r1 = []
while True:
    m = input('Введите наименование товара: ')
    p = input('Введите стоимомть товара: ')
    n = input('Введите количество единиц товара: ')
    r = input('Введите единицу измерения количества: ')
    '''Получает словарь для каждого предмета'''
    dict_product = dict(Наименование=m, Стоимость=p, Количество=n, Единица_измерения=r)
    '''Присваивает словарю свой порядковый номер тем, что номер и сам словарь помещает в кортеж'''
    dict_product
    list_product = [k, dict_product]
    tuple_product = tuple(list_product)
    k += 1
    '''Размещает все кортежи в одном списке'''
    tuple_product
    list_shopping = [tuple_product]
    d.append(tuple_product)
    d
    print(d) # 1-ая часть задания выполнена и выведена на экран
    '''Извлекает то, что находится под первым ключом в словаре у каждого предмета и собирает в словарь'''
    name = dict_product.get('Наименование')
    m1.append(name)
    m1
    dict_name = dict(Наименование=m1)
    '''Извлекает то, что находится под вторым ключом в словаре у каждого предмета и собирает в словарь'''
    price = dict_product.get('Стоимость')
    p1.append(price)
    p1
    dict_price = dict(Стоимость=p1)
    '''Извлекает то, что находится под третьим ключом в словаре у каждого предмета и собирает в словарь'''
    number = dict_product.get('Количество')
    n1.append(number)
    n1
    dict_number = dict(Количество=n1)
    '''Извлекает то, что находится под четвертым ключом в словаре у каждого предмета и собирает в словарь'''
    measure_unit = dict_product.get('Единица_измерения')
    r1.append(measure_unit)
    r1
    dict_measure_unit = dict(Единица_измерения=r1)
    '''Собирает в список все словари'''
    list_specifications = [dict_name, dict_price, dict_number, dict_measure_unit]
    print(list_specifications) # 2-ая часть задания выполнена и выведена на экран


