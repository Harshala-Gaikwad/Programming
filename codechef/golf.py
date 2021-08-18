for _ in range(int(input())):
    N,X,K = map(int, input().split())
    if X%K==0:
        print("YES")
    elif (N+1-X)%K==0:
        print("YES")
    else:
        print("NO")
