for _ in range(int(input())):
    n = int(input())
    l = [1,2,3]
    if n>3:
        for i in range(2,n):
            l.append(l[i-2]+l[i])
    print(l[n-1])
   
