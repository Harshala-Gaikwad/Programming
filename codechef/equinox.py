for _ in range(int(input())):
    n,a,b = map(int, input().split())
    anu = sar = 0
    l = ['E', 'Q', 'U', 'I', 'N', 'O', 'X']
    for i in range(n):
        s = input()
        if s[0] in l: sar+=a
        else: anu+=b
    if anu>sar: print("ANURADHA")
    elif sar>anu: print("SARTHAK")
    else: print("DRAW")
