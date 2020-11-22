class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        i,n= 0,len(nums)
        if not any(map(bool,nums)): return "0"
        nums = list(map(str,nums))
        if len(nums)<2: return "".join(nums)
        while i<len(nums)-1:
            j = i+1
            while j<len(nums):
                if nums[j]+nums[i] > nums[i]+nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
                j+=1
            i+=1
        #nums = [str(nums[i]) for i in range(len(nums))]    
        return "".join(nums)     
                    
        
