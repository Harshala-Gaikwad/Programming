for _ in range(int(input())):
    n,x = map(int, input().split())
    l = list(map(int, input().split()))
    if n-len(set(l))>x: print(len(set(l)))
    else: print(n-x)
        
        
