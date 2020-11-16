class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = set(nums)
        max_ = 0
        max_e = 0
        for i in s:
            if max_< nums.count(i):
                max_ = nums.count(i)
                max_e = i
        return max_e   
