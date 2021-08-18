#User function Template for python3

##Complete this function
def maxSubArraySum(a,size):
    ##Your code here
    max_sum = curr_sum = a[0]
    for i in range(1,len(a)):
        curr_sum = max(a[i]+curr_sum,a[i])
        max_sum = max(curr_sum,max_sum)
    return max_sum    



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            print(maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
