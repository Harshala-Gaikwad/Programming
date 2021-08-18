#{ 
#Driver Code Starts
#Initial Template for Python 3


import math


 # } Driver Code Ends

#User function Template for python3

def exactly3Divisors(N):
    # code here
    total = 0
    prime = True
    for i in range(2,int(N**0.5)+1):
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                prime = False
                break
        if prime and i*i<=N:
            total+=1
        prime = True    
    return total        


#{ 
#Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        
        print(exactly3Divisors(N))
        
        T-=1
    

if __name__=="__main__":
    main()
#} Driver Code Ends
