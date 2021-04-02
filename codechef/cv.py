t= int(input())
l = ['a','e','i','o','u']

while(t!=0):
    n=int(input())
    s=list(input())
    i=0
    c=0
    while(i<len(s)-1):
        if s[i] not in l and s[i+1] in l:
            c=c+1 
            i=i+2
        else:
            i=i+1
    print(c)
    t-=1
            

    
