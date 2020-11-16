class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''nums.sort()
        return nums '''
        n = len(nums)
        l,r,i = 0,n-1,0
        while(i<=r):
            if nums[i] == 0: 
                nums[i],nums[l] = nums[l],nums[i]
                i+=1
                l+=1
            elif nums[i]==2: 
                nums[i],nums[r]=nums[r],nums[i] 
                #i+=1
                r-=1
            else:
                i+=1
        return nums         
            
