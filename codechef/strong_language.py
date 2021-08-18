for _ in range(int(input())):
    n,k = map(int, input().split())
    s = input()
    count = 0
    for i in s:
        if count==k: break
        if i=='*': count+=1
        else: count=0
    if  count>=k: print("YES")
    else: print("NO")
