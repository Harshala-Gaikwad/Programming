for _ in range(int(input())):
    n,m = map(int, input().split())
    x,y = map(int, input().split())
    result = ""
    for i in range(n):
        cand = input()
        if (cand.count('F')>=(x) or cand.count('P') == (x-1)) and cand.count('P')>=y:
            result+='1'
        else:
            result+='0'
    print(result)       
        
