for _ in range(int(input())):
    p = input()
    if p[6:]=='AM' and p[0:2]=='12':
        p = '00'+p[2:]
    elif p[6:]=='PM' and p[0:2]!='12':
        p = str(int(p[0:2])+12)+p[2:]
    #print(p)    
    n = int(input())
    l = []
    for i in range(n):
        time = input()
        h1 = int(time[0:2])
        h2 = int(time[9:11])
        if time[6:8]=='AM' and time[0:2]=='12':
            h1 = '00'
        if time[6:8]=='PM' and time[0:2]!='12':
            h1 = str(h1+12)
            if len(h1)<2:
                h1 = '0'+h1
        if time[15:17]=='AM' and time[9:11]=='12':
            h2 = '00'
        if time[15:17]=='PM' and time[9:11]!='12':
            h2 = str(h2+12)
            if len(h2)<2:
                h2 = '0'+h2
        l.append(str(h1)+time[2:9]+str(h2)+time[11:])    
    s = ''
    for i in l:
        print(i)
        if p[0:2]>= i[0:2] and p[0:2]<=i[9:11]:
            if p[0:2]==i[0:2] and p[3:5]<i[3:5]:
                s+='0'
            elif p[0:2]==i[9:11] and p[3:5]>i[12:14]:
                s+='0'
            else:
                s+='1'
        else:
            s+='0'
    print(s)
