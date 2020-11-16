def isprime(a,b,l1):
    for val in range(a,b):
         if val > 1: 
           for n in range(2, val): 
               if (val % n) == 0: 
                   break
           else: 
               l1.append(val)
    return l1

a,b = map(int ,input().split())
l1 = []
isprime(a,b,l1)
print(l1)

l2 = []
for i in l1:
    for j in l1:
        if(i!=j):
            s = str(i)+str(j)
            l2.append(int(s))

print(l2)

for
        
           
