n = int(input())
l = []
for i in range(1,n+1):
    if i>10:
        break
    elif n%i==0:
        l.append(i)
print(max(l))        
