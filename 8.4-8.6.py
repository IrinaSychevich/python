class Warehouse:
    def __init__(self, quantity_received, sender, quantity_sent, recipient, equipment):
        self.quantity_received = quantity_received
        self.sender = sender
        self.quantity_sent = quantity_sent
        self.recipient = recipient
        self.equipment = equipment

    def logistics(self):
        self.logistics = {'Товар': self.equipment, 'Количество полученных единиц товара': self.quantity_received, 'Отправлено следующим подразделением': self.sender, 'Количество отправленных единиц товара': self.quantity_sent, 'Отправлено в следующее подразделение': self.recipient}
        return self.logistics

    def all_quantity(self):
        q = (int(self.quantity_received) - int(self.quantity_sent))
        return q

from abc import ABC, abstractmethod
class OfficeEquipment(ABC):
    def __init__(self, manufacturer, cost, quantity):
        self.manufacturer = manufacturer
        self.cost = cost
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def all_quantity(self):
        pass

    @abstractmethod
    def new_all_quantity(self, new):
        pass


class Printer(OfficeEquipment):
    def __init__(self, manufacturer, cost, quantity, printing_technology):
        super().__init__(manufacturer, cost, quantity)
        self.printing_technology = printing_technology

    def __str__(self):
        return f"Принтер {self.manufacturer}, стоимость составляет {self.cost} руб., технология печати {self.printing_technology}"

    def all_quantity(self):
        all_quantity = int(self.quantity)
        return all_quantity

    def new_all_quantity(self, new):
        self.quantity = new
        return print(f"Принтер {self.manufacturer}, количество единиц на складе составляет {self.quantity} шт., стоимость составляет {self.cost} руб., технология печати {self.printing_technology}")


class Scanner(OfficeEquipment):
    def __init__(self, manufacturer, cost, quantity, two_way_scanning):
        super().__init__(manufacturer, cost, quantity)
        self.two_way_scanning = two_way_scanning

    def __str__(self):
        return f"Сканер {self.manufacturer}, стоимость составляет {self.cost} руб., двухстороннее сканирование {self.two_way_scanning}"

    def all_quantity(self):
        all_quantity = int(self.quantity)
        return all_quantity
    def new_all_quantity(self, new):
        self.quantity = new
        return print(f"Сканер {self.manufacturer}, количество единиц на складе составляет {self.quantity} шт., стоимость составляет {self.cost} руб., двухстороннее сканирование {self.two_way_scanning}")


class Xerox(OfficeEquipment):
    def __init__(self, manufacturer, cost, quantity, printing_technology, two_way_scanning):
        super().__init__(manufacturer, cost, quantity)
        self.printing_technology = printing_technology
        self.two_way_scanning = two_way_scanning

    def __str__(self):
        return f"Сканер {self.manufacturer}, стоимость составляет {self.cost} руб., технология печати {self.printing_technology}, двухстороннее сканирование {self.two_way_scanning}"

    def all_quantity(self):
        all_quantity = int(self.quantity)
        return all_quantity

    def new_all_quantity(self, new):
        self.quantity = new
        return print(f"Сканер {self.manufacturer}, количество единиц на складе составляет {self.quantity} шт., стоимость составляет {self.cost} руб., технология печати {self.printing_technology}, двухстороннее сканирование {self.two_way_scanning}")



p1 = Printer('Canon', '800', '10', 'лазерная')
p2 = Printer('Epson', '600', '10', 'струйная')
s1 = Scanner('Epson', '700', '10', 'осуществляется')
s2 = Scanner('Plustek', '550', '10', 'отсутствует')
x1 = Xerox('HP', '900', '10', 'струйная', 'отсутствует')



p1_d = [p1.all_quantity()]
p2_d = [p2.all_quantity()]
s1_d = [s1.all_quantity()]
s2_d = [s2.all_quantity()]
x1_d = [x1.all_quantity()]
while True:
    j = input('Введите наименование товара (например, р1): ')
    m = input('Введите количество полученных единиц товара: ')
    try:
        m = int(m)
    except ValueError:
        m = 0
        print('Некорректно введино количество единиц товара!')
    n = input('Введите каким подразделением товар был отправлен: ')
    l = input('Введите количество отправленных единиц товара: ')
    try:
        l = int(l)
    except ValueError:
        l = 0
        print('Некорректно введино количество единиц товара!')
    g = input('Введите в какое подразделение товар был отправлен: ')
    if j == 'p1':
        j = p1
        d = p1_d
    elif j == 'p2':
        j = p2
        d = p2_d
    elif j == 's1':
        j = s1
        d = s1_d
    elif j == 's2':
        j = s2
        d = s2_d
    else:
        j = x1
        d = x1_d
    a_j = Warehouse(m, n, l, g, f'{j}')
    print(a_j.logistics())
    subtraction = a_j.all_quantity()
    d.append(subtraction)
    f = sum(d)
    j.new_all_quantity(f)

