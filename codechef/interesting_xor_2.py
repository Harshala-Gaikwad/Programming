for _ in range(int(input())):
    c = int(input())
    c = bin(c).replace('0b','')
    l = len(c)
    a = "0b1"
    if c[0]=='1': b = "0b0"
    else: b = "0b1"
    b+=('1'*(l-1))
    #print(b)
    for i in range(1,l):
        if c[i]=='0': a+="1"
        else: a+="0"
    print(int(a,2)*int(b,2))
  
