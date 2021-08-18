#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        if n==1:
            return 0
        arr.sort()
        ans = arr[n-1]-arr[0]
        small = arr[0]+k
        big = arr[n-1]-k
        if small>big:
            small,big = big,small
        for i in range(1,n-1):
            sub = arr[i]-k
            add = arr[i]+k
            if (sub>=small) or (add<=big):
                continue
            if (big-sub)<=(add-small):
                small = sub
            else:
                big = add
        return min(ans,big-small)        
            



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
