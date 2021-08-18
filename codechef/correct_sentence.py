for _ in range(int(input())):
    l = list(map(str, input().split()))
    k = int(l[0])
    flag = 0
    for i in range(k):
        if l[i+1].islower():
            if not(all(ord(j) in range(97,110) for j in l[i+1])):
                flag = 1
                break
        elif l[i+1].isupper():
            if not(all(ord(j) in range(78,91) for j in l[i+1])):
                flag=1
                break
        else:
            flag = 1
            break
    if flag==0:
        print("YES")
    else:
        print("NO")
            
