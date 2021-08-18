for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    res = [1,2,3,4,5,6,7]
    count = 0
    for i in a:
        if len(res)==0:
            break
        if i in res:
            res.remove(i)
        count+=1
    print(count)    
