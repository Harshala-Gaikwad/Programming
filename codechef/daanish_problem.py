for _ in range(int(input())):
    l = list(map(int,input().split()))
    k = int(input())
    i = len(l)-1
    while l[i]<=k:
        k -= l[i]
        l.pop(i)
        i-=1
    print(len(l))    
