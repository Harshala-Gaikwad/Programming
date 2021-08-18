def mul(n,res,size):
    carry = 0
    for i in range(size):
        prod = res[i]*n+carry
        res[i] = prod%10
        carry = prod//10
    while carry:
        res[size] = carry%10
        carry //= 10
        size+=1
    return size

def fac(n):
    res = [0]*500
    res[0] = 1
    size = 1
    for i in range(2,n+1):
        size = mul(i,res,size)
    s = ''    
    for i in range(size-1,-1,-1):
        s+=str(res[i])
    print(int(s))
for _ in range(int(input())):
    n = int(input())
    fac(n)
    
'''
for _ in range(int(input())):
    n = int(input())
    f = 1
    for i in range(2,n+1):
        f*=i
    print(f)  '''  
    
