class Stationery():
    title = ('ручка', 'карандаш', 'маркер')

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    title = Stationery.title[0]
    def draw(self):
        print('Используй ручку')


class Pencil(Stationery):
    title = Stationery.title[1]
    def draw(self):
        print('Используй карандаш')


class Handle(Stationery):
    title = Stationery.title[2]
    def draw(self):
        print('Используй маркер')


a = Pen()
print(a.title)
a.draw()


b = Pencil()
print(b.title)
b.draw()


c = Handle()
print(c.title)
c.draw()