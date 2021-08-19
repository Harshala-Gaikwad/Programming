import math
s = 'iffactsdontfittotheorychangethefacts'
n = len(s)
l = int(math.sqrt(n))
r = l+1
print(l,r)
result = []
for i in range(r):
    temp = []
    j = 0
    while i+j<n:
        temp.append(s[i+j])
        j+=r
    result.append("".join(temp))
print(" ".join(result))    
