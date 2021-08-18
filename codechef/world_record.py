for _ in range(int(input())):
    l = list(map(float, input().split()))
    time = round((100/(l[0]*l[1]*l[2]*l[3])),2)
    if time<9.58: print("YES")
    else: print("NO")
