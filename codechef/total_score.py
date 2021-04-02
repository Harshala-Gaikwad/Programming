for _ in range(int(input())):
    n,k = map(int, input().split())
    l = list(map(int, input().split()))
    for i in range(n):
        result = 0
        s = input()
        for i in range(len(s)):
            if s[i]=='1':
                result+=l[i]
        print(result)        
