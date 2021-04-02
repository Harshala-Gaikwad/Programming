for _ in range(int(input())):
    n = int(input())
    s = input()
    one = s.count("1")
    total = one+(120-n)
    res = (total/120)*100
    if res>=75:
        print("YES")
    else:
        print("NO")
