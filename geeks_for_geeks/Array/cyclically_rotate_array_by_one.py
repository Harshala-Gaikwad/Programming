for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    print(l[-1],end=" ")
    for i in range(len(l)-1):
        print(l[i],end=" ")
    print()    
