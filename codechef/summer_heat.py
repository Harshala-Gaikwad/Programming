for _ in range(int(input())):
    x1,x2,X1,X2 = map(int, input().split())
    res = (X1//x1) + (X2//x2)
    print(res)
