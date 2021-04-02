for _ in range(int(input())):
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    i = 0
    while i<n:
        if sum(A)>sum(B):
            break
        else:
            min(A),max(B) = min
        i+=1
        
