for _ in range(int(input())):
    l = input().split()
    x = int(l[0])
    y = l[1]
    week = ['mon','tue','wed','thu','fri','sat','sun']
    l2 = [4]*7
    ind = week.index(y)
    days = {28:0,29:1,30:2,31:3}
    for i in range(days[x]):
        l2[ind]+=1
        ind+=1
        if ind==7:
            ind=0
    print(*l2)        
