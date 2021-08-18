n = int(input())
l = list(map(int, input().split()))
q = int(input())
l1 = list(map(int, input().split()))
k = 0
for i in range(q):
    n = len(l)
    x = abs(l1[k])
    temp = l[n-x:n]+l[:n-x]
    l.extend(temp)
    print(sum(l))
    k+=1
    
