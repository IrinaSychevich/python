from itertools import count, cycle
from sys import argv
script_name, a, my_list = argv
a = int(a)
for el in count(a):
    if el > 10:
        break
    else:
        print(el)
с = 0
for el in cycle(my_list):
    if с > 10:
        break
    print(el)
    с += 1