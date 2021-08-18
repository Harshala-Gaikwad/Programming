class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i,num in enumerate(nums) :
            if num not in d:
                d[num] = i
            else:
                del d[num]
        for i in d:
            return i
                
        
