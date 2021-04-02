for _ in range(int(input())):
    a,b,c = map(str,input().split())
    if a == 'A':
        print(b.lower()+c.capitalize())
    elif a == 'B':
        print(b.lower()+'_'+c.lower())
    elif a == 'C':
        print(b.upper()+'_'+c.upper())
    elif a == 'D':
        print(b.capitalize()+'-'+c.capitalize())
    else:
        ans = ""
        for i in range(len(b)):
            if i%2==0:
                ans += b[i].lower()
            else:
                ans += b[i].upper()
        ans+="|"
        for i in range(len(c)):
            if i%2==0:
                ans += c[i].lower()
            else:
                ans += c[i].upper()
        print(len(ans))        
