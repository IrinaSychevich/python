my_list = [10, 5, 4, 3, 2]
n = int(input('Напишите число: '))
m = len(my_list)-1
if n <= my_list[m]:
    my_list.insert(m + 1, n)
elif n > my_list[0]:
    my_list.insert(0, n)
else:
    while my_list[m] < n:
        if my_list[m - 1] >= n:
            my_list.insert(m, n)
        m = m - 1
print(my_list)