import math
for _ in range(int(input())):
    D,d,p,q = map(int, input().split())
    temp = s = 0
    count = D
    for i in range(0,D,d):
        if count>d:
            s+= (p + temp*q)*d
        else:
            s+= (p + temp*q)*count
        temp += 1
        count -= d
        
    print(s)    
        
        
        
