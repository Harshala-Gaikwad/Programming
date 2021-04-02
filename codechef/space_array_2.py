for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    j = 1
    flag = count = 0
    i = 0
    while i<n:
        if l[i]>j:
            flag = 1
            break
        elif l[i]==j:
            i+=1
            j+=1
        else:
            count+=1
            l[i]+=1
            if l[i]==j:
                i+=1
                j+=1
                
    if flag==1 or count%2==0:
        print("Second")
    else:
        print("First")
    
            
            
