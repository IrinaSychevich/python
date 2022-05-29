f = open(r"new_f_5.3.txt", 'r', encoding='utf-8')
content = f.readlines()
len_content = len(content)
all_name_l_salary = []
all_salary = []
for el in content:
    el = el.split(' ')
    name = el[0]
    salary = float(el[1])
    if salary < 20000:
        name
        all_name_l_salary.append(name)
    all_salary.append(salary)
print('Сотрудники с заработной платой меньше 20000: ')
for el in all_name_l_salary:
    print(el)
average_salary = round((sum(all_salary) / len_content), 2)
print(f'Средняя заработная плата: {average_salary}')
f.close()
