class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums)==0: return 1
        m = max(nums)
        for x in range(1,m+2):
            if x not in nums: return x
        return 1    
        
