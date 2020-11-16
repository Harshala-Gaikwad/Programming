for i in range(int(input())):
    n = int(input())
    s = input()
    s1 = set(s)
    flag =1
    for j in s1:
        if(s.count(j)%2!=0):
            flag = 0    
    if flag==1:
        print("YES")
    else:
        print("NO")
