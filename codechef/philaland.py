cases=int(input())

for i in range(1,cases+1):
    value=int(input())
    
    coincount = 0
    
    while value>=1:
        value=value//2
        coincount=coincount+1
        
    #print the answer    
    print (coincount)
