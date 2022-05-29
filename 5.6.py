f1 = open(r"new_f_5.6.txt", 'r', encoding='utf-8')
content = f1.readlines()
all_title = []
all_my_sum = []
for el in content:
    el = el.split(' ')
    title = el[0]
    title = title[0:(len(title)-1)]
    l = el[1]
    pr = el[2]
    lab = el[3]
    l1 = len(l)-1
    while l1 >= 0:
        if ord(l[l1]) not in range(48,58):
            l = l[0:(l1)]
        l1 -=1
    pr1 = len(pr) - 1
    while pr1 >= 0:
        if ord(pr[pr1]) not in range(48, 58):
            pr = pr[0:(pr1)]
        pr1 -= 1
    lab1 = len(lab) - 1
    while lab1 >= 0:
        if ord(lab[lab1]) not in range(48, 58):
            lab = lab[0:(lab1)]
        lab1 -= 1
    if len(l) > 0:
        l = int(l)
    else:
        l = 0
    if len(pr) > 0:
        pr = int(pr)
    else:
        pr = 0
    if len(lab) > 0:
        lab = int(lab)
    else:
        lab = 0
    my_sum = l + pr + lab
    all_my_sum.append(my_sum)
    all_title.append(title)
my_dict = {}
k = 0
while k < len(all_title):
    my_dict.update({all_title[k]: all_my_sum[k]})
    k += 1
print(my_dict)