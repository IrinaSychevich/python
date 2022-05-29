f_obj = open("new_f_5.1.txt", 'w')
while True:
    my_data = input('Введите данные: ')
    my_list_data = [my_data, '\n']
    f_obj.writelines(my_list_data)
    if len(my_data) == 0:
        break
f_obj.close()
