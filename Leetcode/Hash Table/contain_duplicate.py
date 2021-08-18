class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        f = 1
        for i,num in enumerate(nums):
            if num not in d:
                d[num]=i
            else:
                return True
        return False    
        
