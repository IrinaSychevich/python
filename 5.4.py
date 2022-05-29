f1 = open(r"new_f_5.4.txt", 'r', encoding='utf-8')
content = f1.readlines()
all_sign = []
all_number = []
for el in content:
    el = el.split(' ')
    sign = el[1]
    number = el[2]
    all_sign.append(sign)
    all_number.append(number)
all_sign
all_number
f2 = open(r"new_f_5.4.b.txt", 'w', encoding='utf-8')
all_name_rus = ['Один', 'Два', 'Три', 'Четыре']
m = 0
while m < len(all_name_rus):
    line_1 = []
    line_1.append(all_name_rus[m])
    line_1.append(all_sign[m])
    line_1.append(all_number[m])
    line_1 = ' '.join(line_1)
    m += 1
    f2.write(line_1)
