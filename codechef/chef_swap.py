for t in range(int(input())):
    n = int(input())
    l1 = list(map(int , input().split()))
    l2 = list(map(int, input().split()))
    l1.sort()
    l2.sort()
    if(l1==l2):
        print(0)    
    else:
        count=0
        for i in range(n):
            if(l1[i]!=l2[i]):
                for j in range(i+1,n):
                    if(l2[i]==l2[j]):
                        count+=min(l1[i],l2[j])
                        temp = l1[i]
                        l1[i] = l2[j]
                        l2[j] = temp
        if(l1==l2):
            print(count)
        else:
            print(-1)
               
