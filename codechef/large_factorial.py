def mul(n):
    n = list(str(n)[::-1])
    #print(n)
    carry = 0
    for i in range(len(n)):
        prod = ((int(n[i])*10)+carry)
        print(prod)
        n[i]=prod%10
        carry = prod//10
    if carry!=0:
        n.append(carry)
    n.reverse()
    res = 0
    for i in range(len(n)):
        res = res*10+n[i]%10
    return(res)
def fact(n):
    i = n
    while i>1:
        p = mul(i)
        i-=1
    return     
    
for _ in range(int(input())):
    n = int(input())

        
