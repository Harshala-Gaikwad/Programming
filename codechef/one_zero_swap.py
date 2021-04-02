for _ in range(int(input())):
    n = int(input())
    s = input()
    p = input()
    d = {'0':0,'1':0}
    d1 = {'0':0,'1':0}
    for i in s:
        if i in d:
            d[i] = d[i]+1
        else:
            d[i] = 1
    for i in p:
        if i in d1:
            d1[i] = d1[i]+1
        else:
            d1[i] = 1
    #print(d['0'])
    #print(d['1'])
    #print(d1)
    if d['0']==d1['0'] and d['1']==d1['1']:
        print("Yes")
    else:
        print("No")
            
