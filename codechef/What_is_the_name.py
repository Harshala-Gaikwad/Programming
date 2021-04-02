for _ in range(int(input())):
    s = input().split()
    if len(s)==1:
        print(str(s[0]).capitalize())
    elif len(s)==2:
        print(str(s[0][0]).upper()+". "+str(s[1]).capitalize())
    elif len(s)==3:
        print(str(s[0][0]).upper()+". "+str(s[1][0]).upper()+". "+str(s[1]).capitalize())    
        
