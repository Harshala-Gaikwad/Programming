for _ in range(int(input())):
    n = int(input())
    s = input()
    r=b=g=0
    for i in s:
        if i=="R":
            r+=1
        elif i=="B":
            b+=1
        else:
            g+=1
    m = max(r,b,g)
    print(n-m)
        
