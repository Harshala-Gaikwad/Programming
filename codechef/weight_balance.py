for _ in range(int(input())):
    w1,w2,x1,x2,m = map(int, input().split())
    weight = w2-w1
    min_ = x1*m
    max_ = x2*m
    if (min_<weight<max_) or (weight==min_ or weight==max_):
        print(1)
    else:
        print(0)
