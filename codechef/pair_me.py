for _ in range(int(input())):
    l = list(map(int,input().split()))
    m = max(l)
    mx_ = l.pop(l.index(m))
    if mx_==sum(l):
        print("YES")
    else:
        print("NO")
    
