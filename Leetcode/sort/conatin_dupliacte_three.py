class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t<0 or k<=0 or len(nums)==0:
            return False
        bucket = {}
        width = t+1
        for n, i in enumerate(nums):
            buck = i//width
            if buck in bucket:
                return True
            else:
                bucket[buck]=i
                if buck - 1 in bucket and i - bucket[buck-1] <= t:
                    return True
                if buck + 1 in bucket and bucket[buck+1] - i <= t:
                    return True
                if n >= k:
                    del bucket[nums[n-k] // width]
        return False            
        
