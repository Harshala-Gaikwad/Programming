t = int(input())
while(t>0):
    s = input()
    c = set()
    l = []
    for i in range(len(s)):
        if s[i] not in c:
            c.add(s[i])
            l.append(ord(s[i]))
    print(c)
    print(l)
    t -=1
