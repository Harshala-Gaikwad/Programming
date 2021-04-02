for _ in range(int(input())):
    s = input()
    count = flag = 0
    if s.count('1')==0:
        print(0)
    else:
        for i in s:
            if i=='1' and flag==0:
                flag = 1
                count+=1
            elif i=='0':
                flag = 0
        print(count)        
