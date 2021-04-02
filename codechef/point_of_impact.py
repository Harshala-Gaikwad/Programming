for _ in range(int(input())):
    n,k,x,y = map(int,input().split())
    if x==y:
        print(n,n)
    elif x>y:
        l = [[n,n-x+y],[n-x+y,n],[0,x-y],[x-y,0]]
        l1 = l[(k%4)-1]
        #print(l1)
        print(l1[0],l1[1])
    else:
        l = [[x+n-y,n],[n,x+n-y],[y-x,0],[0,y-x]]
        l1 = l[(k%4)-1]
        print(l1[0],l1[1])
        
