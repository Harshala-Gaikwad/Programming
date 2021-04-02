R,O,C = map(int, input().split())
if C>R or (((20-O)*6*6)+C)>R: 
    print("YES")
else:
    print("NO")
    
