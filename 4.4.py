l1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
generator = [l1[i] for i in range(len(l1)) if not (l1[i] in l1[0: i] or l1[i] in l1[i+1: len(l1)])]
print(generator)