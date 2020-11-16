class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        s = set(nums)
        if len(s)<3:
            return max(s)
        mx1 = max(s)
        s.remove(mx1)
        mx2 = max(s)
        s.remove(mx2)
        return max(s)
