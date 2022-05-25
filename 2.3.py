month = int(input('Введите месяц через число: ')) # 1 способ
timeofyear = {1 : 'зима', 2 : 'зима', 3 : 'весна', 4 : 'весна', 5 : 'весна', 6 : 'лето', 7 : 'лето', 8 : 'лето', 9 : 'осень', 10 : 'осень', 11 : 'осень', 12 : 'зима'} # 1 способ
print(f'{month} - {timeofyear.setdefault(month)}') # 1 способ

mon = int(input('Введите месяц через число:')) # 2 способ
time = ['зима', 'весна', 'лето', 'осень'] # 2 способ
if mon in [1, 2, 12]:
    print(f'{month} - {time[0]}')
elif mon in [3, 4, 5]:
    print(f'{month} - {time[1]}')
elif mon in [6, 7, 8]:
    print(f'{month} - {time[2]}')
elif mon in [9, 10, 11]:
    print(f'{month} - {time[3]}')