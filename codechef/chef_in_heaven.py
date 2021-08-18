for _ in range(int(input())):
    l = int(input())
    s = input()
    good = bad = flag = 0
    for i in s:
        if i== '1': good+=1
        else: bad+=1
        if good>=bad: flag = 1
    if flag==1: print("YES")
    else: print("NO")
