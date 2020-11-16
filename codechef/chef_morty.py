import math
def findSum(num,sum_):
    while(num!=0):
        sum_+=(num%10)
        num = num/10
    return sum_

for i in range(int(input())):
    n = int(input())
    l1 = []
    l2 = []
    chef=0
    morty =0
    for i in range(n):
        x,y = input().split()
        l1.append(int(x))
        l2.append(int(y))
        if(math.floor(math.log(l1[i],10)+1)>1):
            l1[i] = findSum(l1[i],0)
        if(math.floor(math.log(l2[i],10)+1)>1):
            l2[i] = findSum(l2[i],0)
        if(l1[i]>l2[i]):
            chef+=1
        if(l1[i]<l2[i]):
            morty+=1
    if(chef>morty):
         print(0,chef)
    elif(chef<morty):
         print(1,morty)
    else:
         print(2,chef)
     
               
