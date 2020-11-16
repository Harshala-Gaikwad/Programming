class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = sum(nums[:3])
        for i in range(len(nums)-2):
            j,k = i+1,n-1
            while(j<k):
                s = nums[i]+nums[j]+nums[k]
                if abs(s-target)<abs(res-target):
                    res = s
                if s<target:
                    j+=1
                else:
                    k-=1
        return res  
