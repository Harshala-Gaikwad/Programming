A = [4,1,3,2]
i,j = 0,1
while i<j:
    if A[i]>A[j]:
        j-=1
    else:
        i+=1
X = A[:i+1]
Y = A[j+1:]
#print(Y)
Y = Y[::-1]
#print(X)
#print(Y)
X.extend(Y)
print(X)
