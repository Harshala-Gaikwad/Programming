for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    flag = 0
    l1 = []
    for i in range(n):
        l1.append(i+1)
    i=count=0
    while l!=l1:
        if l[i]<l1[i]:
            l[i]+=1
            count+=1
        elif l[i]==l1[i]:
            i+=1
        elif l[i]>l1[i]:
            flag = 1
            break
    if count%2==0 or flag==1:
        print("Second")
    else:
        print("First")
    
            
            
