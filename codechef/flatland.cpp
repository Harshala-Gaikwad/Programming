t = int(input())
for i in range(t):
    n = int(input())
    count=0
    while(n!=0):
        n = n - int(math.sqrt(n))**2
        count+=1
    print(count)    
