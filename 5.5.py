my_f = open("new_f_5.5.txt", "w+", encoding='utf-8')
my_f.write(input('Введите значения через пробел: '))
my_f.seek(0)
content = my_f.read()
list_content = content.split(' ')
m = 0
new_list_content = []
while m < len(list_content):
    a = int(list_content[m])
    new_list_content.append(a)
    m += 1
my_sum = sum(new_list_content)
print(my_sum)
my_f.write('\n'f'Сумма чисел равна {my_sum}')
