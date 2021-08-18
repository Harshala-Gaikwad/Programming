for _ in range(int(input())):
    x,y,xr,yr,d = map(int, input().split())
    if min(x/xr, y/yr)>=d:
        print("YES")
    else:
        print("NO")
