class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        if len(nums)==0:
            return 0
        if len(nums)<3:
            return max(nums)
        
        nums.sort()
        return nums[len(nums)-3]
