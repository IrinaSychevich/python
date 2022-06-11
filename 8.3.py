class NumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

a = [8, 'vr', 15 , 20, True, 5]
y = []
while True:
    x = input('Введите число: ')
    if x == 'stop':
        break
    else:
        try:
            for el in x:
                if ord(el) > 57 or ord(el) < 48:
                    raise NumberError('Вы ввели не число!')
        except NumberError as err:
            print(err)
        else:
            y.append(x)
            print(y)
