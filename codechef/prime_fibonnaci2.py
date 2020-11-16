def isPrime(x):
    i = 2
    while(i< x/2+1):
        if(x%i == 0):
            return 0
        i+=1
    else:
        return 1

def fibonnaci(min_,max_,n):
    t1 = min_
    t2 = max_
    count = 2
    for i in range(3,n+1):
        temp = t1+t2
        t1 = t2
        t2 = temp
    print(temp)    

a,b = map(int, input().split())
l1 = []
for i in range(a,b):
    if isPrime(i) == 1:
        l1.append(i)

#print(l1)        
l2 = []
for i in l1:
    for j in l1:
        if(i!=j):
            s = str(i)+str(j)
            l2.append(int(s))

#print(l2)
l3 = []
for i in l2:
    if ((isPrime(i)==1) and (i not in l3)):
        l3.append(i)
#print(l3)
l1.clear()
l2.clear()
min_ = min(l3)
max_ = max(l3)
#print(min_)
#print(max_)
fibonnaci(min_,max_,len(l3))
l3.clear()
