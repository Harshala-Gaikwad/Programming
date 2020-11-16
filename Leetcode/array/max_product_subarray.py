class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min = curr_max = prev_max = prev_min = result = nums[0]
        
        for i in range(1,len(nums)):
            curr_max = max(prev_max*nums[i],prev_min*nums[i],nums[i])
            curr_min = min(prev_max*nums[i],prev_min*nums[i],nums[i])
            result = max(curr_max,result)
            prev_max = curr_max
            prev_min = curr_min
        return result    
        
