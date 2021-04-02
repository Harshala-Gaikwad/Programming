N,H,X = map(int,input().split())
l = list(map(int,input().split()))
l.sort(reverse=True)
flag = 0
for i in l:
    if i+X>=H:
        flag = 1
        print("YES")
        break
if flag==0:
    print("NO")
        
