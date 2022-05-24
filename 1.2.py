time = int(input('Введите длительность фильма в секундах: '))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - hours * 3600 - minutes * 60 # 1 способ
sec = time % 60 # 2 способ
print(f'{"%.2d" % hours}:{"%.2d" % minutes}:{"%.2d" % seconds}') # 1 способ
print(f'{"%.2d" % hours}:{"%.2d" % minutes}:{"%.2d" % sec}') # 2 способ