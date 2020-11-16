T = int(input())
def count(x):
    sum = 0
    while(x>0):
        sum = sum + x%10
        x=x//10
    return sum

for i in range(T):
    N = int(input())
    cp = 0
    mp = 0
    for j in range(N):
        A,B =  map(int, input().split())
        chef = count(A)
        morty = count(B)
        if(chef>morty):
            cp+=1
        elif(morty>chef):
            mp+=1
        elif(chef == morty):
            cp+=1
            mp+=1       
    if(cp>mp):
        print(0,cp)
    if(mp>cp):
        print(1,mp)
    if(mp==cp):
        print(2,mp)
