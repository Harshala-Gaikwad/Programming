class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)<4:
            return []
        n = len(nums)
        nums.sort()
        result = []
        for i in range(n-3):
            if i>0 and nums[i]== nums[i-1]:
                continue
            j = i+1  
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]: continue
                left,right = j+1,n-1
                while(left<right):
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s== target:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        right-=1
                        while(left<right and nums[left]==nums[left-1]):
                            left+=1
                        while(left<right and nums[right]==nums[right+1]):
                            right-=1
                    elif s<target:
                        left+=1
                    else:    
                        right-=1
        return result                
                        
