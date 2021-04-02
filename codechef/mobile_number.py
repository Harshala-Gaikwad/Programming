for _ in range(int(input())):
    s = input()
    if (s[0]!='0') and (len(s)==10) and (s.isdigit()):
        print("YES")
    else:
        print("NO")
