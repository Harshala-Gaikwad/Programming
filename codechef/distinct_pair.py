import math
for _ in range(int(input())):
    l,r = map(int,input().split())
    total = r-l+1
    print(sum(range(1,r-l+2)))

