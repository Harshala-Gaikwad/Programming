#code
for _ in range(int(input())):
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    l = []
    for i in range(n):
        if A[i] not in l:
            l.append(A[i])
    for i in range(m):
        if B[i] not in l:
            l.append(B[i])
    print(len(l))        
