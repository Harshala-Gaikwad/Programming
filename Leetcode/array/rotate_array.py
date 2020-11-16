class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''j = 0
        for i in range(len(nums)-k,len(nums)):
            nums[i],nums[j] = nums[j],nums[i]
            j+=1 '''
        if len(nums)<k:
            k = k-len(nums)
            
        #if len(nums)>=k:
        nums.reverse()
        i,j = 0,k-1
        while i<j:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j-=1
        i,j=k,len(nums)-1
        while i<j:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j-=1 
