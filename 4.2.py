l1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
l2 = [l1[i] for i in range(len(l1)) if l1[i] > l1[i-1]]
print(l2)