for _ in range(int(input())):
    n,k,d = map(int,input().split())
    A = list(map(int,input().split()))
    s = sum(A)//k
    if s<d:
        print(s)
    else:
        print(d)
