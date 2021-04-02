for _ in range(int(input())):
    s = input()
    if len(s)<10:
        print("NO")
    else:    
        s1 = set(s)
        flag = 0
        for i in s1:
            if i.islower():
                flag = 1
            elif i.isupper():
                flag = 1
            elif i.isdigit():
                flag= 1
            elif i in ['@','#','%','&','?']:
                flag = 1
            else:
                flag = 0
                break
        if flag==1:
            print("YES")
        else:
            print("NO")
            
