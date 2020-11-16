t = int(input())
while(t>0):
    ans = "YES"
    n = int(input())
    l = list(map(int, input().split()))
    for i in range(n):
        if(l[i]%2==0):
            ans = "NO"
            break;
        else:
            ans = "YES"
    print(ans)
    t-=1
