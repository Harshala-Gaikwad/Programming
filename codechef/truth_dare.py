t=int(input())
flag="yes"
while(t>=0):
    tr=int(input())
    Tr = list(map(int,input().split()))
    dr=int(input())
    Dr = list(map(int,input().split()))
    ts=int(input())
    Ts = list(map(int,input().split()))
    ds=int(input())
    Ds = list(map(int,input().split()))
    for i in Ts:
        if i not in Tr:
            flag="no"
            break
    for i in Ds:
        if i not in Dr:
            flag="no"
            break
    print(flag)
    flag = "yes"
    t-=1    
