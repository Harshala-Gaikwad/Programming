for _ in range(int(input())):
    n,x = map(int, input().split())
    l = []
    l = [list(map(int, input().split())) for i in range(n)]
    #print(l)
    new_l = []
    for i in range(n):
        if l[i][0]<=x:
            new_l.append(l[i][1])
    print(max(new_l))        
