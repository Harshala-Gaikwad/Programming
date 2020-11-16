class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        l = []
        n = len(nums)
        for i in range(n):
            if nums[i] in l:
                return nums[i]
            l.append(nums[i])
        '''
        nums.sort()
        n = len(nums)
        for i in range(n):
            if nums[i]==nums[i+1]:
                return nums[i]    
