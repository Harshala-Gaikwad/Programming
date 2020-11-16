class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = 0
        i = 0
        l = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(target==nums[i]+nums[j]):
                     return [i,j]           
            
