for _ in range(int(input())):
    n,m = map(int, input().split())
    l = list(map(int, input().split()))
    l = set(l)
    if len(l)<m:
        print("Yes")
    else:
        print("No")
