def sub(l):
    base = []
    lists = [base]
    for i in range(len(l)):
        orig = lists[:]
        new = l[i]
        for j in range(len(lists)):
            lists[j] = lists[j] + [new]
        lists = orig + lists
    return lists


l1 = [1,2,3,1,2,3]
d = 38
l2 = sub(l1)
r = []
print(l2)
'''
for a in l2:
    if sum(a) >= d:
        r.append(a)
print(r)
'''
