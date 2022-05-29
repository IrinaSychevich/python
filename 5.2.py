f = open("new_f_5.2.txt", 'r')
content = f.readlines()
len_content = len(content)
print(f'Количество строк в файле равно {len_content}')
n = 1
for el in content:
    el = el.split(' ')
    len_el = len(el)
    print(f'Количество слов в строке {n} равно {len_el}')
    n +=1
f.close()
