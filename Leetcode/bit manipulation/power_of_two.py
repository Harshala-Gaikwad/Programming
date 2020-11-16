class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        while n>0:
            count+=1
            n = n&(n-1)
        if count==1:
            return True
        else:
            return False
        
