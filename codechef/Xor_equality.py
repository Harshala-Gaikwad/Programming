for _ in range(int(input())):
    n = int(input())
    x = 2
    temp = 1
    y = n-1
    while y>0:
        if y%2 != 0:
            temp = temp*x
        x = x**2
        y = y//2
    print(temp)    
