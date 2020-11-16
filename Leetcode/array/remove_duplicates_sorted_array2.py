class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = []
        for i in nums:
            if l.count(i)<2:
                l.append(i)
        nums.clear()
        for i in l:
            nums.append(i)
        return len(nums)    
        
