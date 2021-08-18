for _ in range(int(input())):
    D,d,a,b,c = map(int, input().split())
    res = D*d
    if 10<=res<21:
        print(a)
    elif 21<=res<42:
        print(b)
    elif res>=42:
        print(c)
    else:
        print(0)
        
