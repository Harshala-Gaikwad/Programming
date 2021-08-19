n = len(w)
    w = list(w)
    i = n-2
    s = ""
    while i>=0 and w[i]>=w[i+1]:
        i-=1
    if i== -1:
        s = "no answer"
    else:
        j = n-1
        while j>=i and w[j]<=w[i]:
            j-=1
        w[i],w[j] = w[j],w[i]  
        w = "".join(w)      
        s =  w[:i+1]+w[i+1:][::-1]
    return s   
