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
        h1 = time[0:8]
        h2 = time[9:17]
        if h1[6:8]=='AM' and h1[0:2]=='12':
            h1 = '00'+h1[2:]
        elif h1[6:8]=='PM' and h1[0:2]!='12':
            h1 = str(int(h1[0:2])+12)+h1[2:]
        else:
            h1 = h1[:]
            
        if h2[6:8]=='AM' and h2[0:2]=='12':
            h2 = '00'+h2[2:]
        elif h2[6:8]=='PM' and h2[0:2]!='12':
            h2 = str(int(h2[0:2])+12)+h2[2:]
        else:
            h2 = h2[:]    
        l.append(h1+h2)
    
    s = ''
    for i in l:
        #print(i)
        if p[0:2]>= i[0:2] and p[0:2]<=i[8:10]:
            if p[0:2]==i[0:2] and p[3:5]<i[3:5]:
                s+='0'
            elif p[0:2]==i[8:10] and p[3:5]>i[11:13]:
                s+='0'
            else:
                s+='1'
        else:
            s+='0'

    print(s)
