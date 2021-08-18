mod = 10**9+7
def power(a,b):
    res = 1
    while(b>0):
        if b%2==1:
            res*=a%mod
        a*=a%mod
        b//=2
    return res%mod    

for _ in range(int(input())):
    n,m = map(int, input().split())
    res = power(power(2,n)-(1%mod),m)
    print(res)
 
