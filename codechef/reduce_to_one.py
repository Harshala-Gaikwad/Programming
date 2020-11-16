l =[0]
f=1
for i in range(1,10**6+1):
        f = (f*(i+1)%(10**9+7))
        l.append(f)
        
t = int(input())
for i in range(t):
    n = int(input())
    print(l[n]-1)
