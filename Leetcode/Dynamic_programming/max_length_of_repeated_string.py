class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        t = ([[0 for i in range(m+1)] for i in range(n+1)])
        res = 0
        for i in range(1, n+1):
            for j in range(1,m+1):
                if nums1[i-1]==nums2[j-1]:
                    t[i][j] = 1+t[i-1][j-1]
                    res = max(res, t[i][j])
                else:
                    t[i][j] = 0
        return res           
        
