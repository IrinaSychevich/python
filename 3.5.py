d = 0
while True:
    l1 = input('Введите числа через пробел: ')
    l2 = l1.split(' ')
    def my_func1(l2):
        l2
        m = len(l2) - 1
        try:
            while m >= 0:
                l2[m] = int(l2[m])
                l2.insert(m, l2[m])
                l2.pop(m + 1)
                m -= 1
            l2
            my_sum = sum(l2)
            return my_sum
        except ValueError:
            if "s" in l2:
                k = 0
                t = l2.index('s')
                while k < t:
                    l2[k] = int(l2[k])
                    l2.insert(k, l2[k])
                    l2.pop(k + 1)
                    k += 1
                l2
                w = len(l2) - 1
                while w >= t:
                    l2.pop(w)
                    w -= 1
                l2
                my_sum = sum(l2)
                return my_sum
            else:
                return
    sum_of_number = my_func1(l2)
    sum_of_num = sum_of_number
    try:
        sum_of_number = int(sum_of_number)
    except TypeError:
        break
    print(sum_of_num)
    sum_of_num = sum_of_num + d
    d += sum_of_number
    print(sum_of_num)
    if "s" in l1:
        break