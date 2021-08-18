'''n,q = map(int, input().split())
l = list(map(int, input().split()))
for i in range(q):
    sum = 1
    x = int(input())
    for j in range(n):
        sum *= (x-l[j])
    if sum>0:
        print("POSITIVE")
    elif sum<0:
        print("NEGATIVE")
    else:
        print("0")'''
import math
n,q = map(int, input().split())
l = list(map(int, input().split()))       
l.sort(reverse=True)
jump = int(math.sqrt(n))     
for i in range(q):
    x = int(input())
    pos = 0
    while(((pos+jump)<n) and ((l[pos+jump])>x)): pos+=jump
    while pos<n and l[pos]>x:
        pos+=1
     
    if (x in l):
        print("0")
    elif pos%2==0:
        print("POSITIVE")
    else:
        print("NEGATIVE")
