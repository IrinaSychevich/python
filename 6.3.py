class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {'wage': self.wage, 'bonus': self.bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    def get_full_name(self):
        get_full_name = self.name + ' ' + self.surname
        print(get_full_name)
    def get_total_income(self):
        get_total_income = self._income.get('wage') + self._income.get('bonus')
        print(get_total_income)

b = Position('Иван', 'Сидоров', 'инженер', 800, 250)
print(b.name)
print(b.surname)
print(b.position)
print(b._income)
b.get_full_name()
b.get_total_income()