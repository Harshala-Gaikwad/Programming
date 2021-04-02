for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    x,y,z = 0,1,n-1
    #print(l[x],l[y],l[z])
    ans = abs(l[x]-l[y])+ abs(l[y]-l[z]) + abs(l[z]-l[x])
    print(ans)
