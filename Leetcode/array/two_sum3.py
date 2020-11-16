class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers)<2:
            return []
        n = len(numbers)
        l,r = 0,n-1
        while l<r :
            if numbers[l]+numbers[r]== target: return [l+1,r+1]
            elif numbers[l]+numbers[r]<target: l+=1
            else: r-=1    
        
