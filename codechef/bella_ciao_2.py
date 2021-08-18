for _ in range(int(input())):
    D,d,p,q = map(int, input().split())
    n = D//d
    #s = ((n*0.5)*((2*p)+(n-1)*q))*d
    s = ((p*n)+(q*(n-1)*n*0.5))*d
    rem = D%d
    if rem!=0:
        s += (rem*(p+n*q))
    print(int(s))
    
s = ((p*n)+(q*(n-1)*n*0.5))*d
