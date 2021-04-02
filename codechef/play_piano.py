for _ in range(int(input())):
    s = input()
    flag =1
    for i in range(0,len(s),2):
        if s[i]==s[i+1]:
            print("no")
            flag = 0
            break
    if flag==1:
        print("yes")
