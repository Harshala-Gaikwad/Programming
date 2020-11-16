class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = []
        max_yet = nums[0]
        max_sum.append(nums[0])
        for i in range(1,len(nums)):
            max_sum.append(max(max_sum[i-1]+nums[i],nums[i]))
        max_yet = max(max_sum)
        return max_yet
        
