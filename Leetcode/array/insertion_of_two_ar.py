class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set()
        n1,n2 = len(nums1),len(nums2)
        if n1>=n2:
            for i in range(n2):
                if nums2[i] in nums1 and nums2[i] not in s:
                    s.add(nums2[i])
        else:
            for i in range(n1):
                if nums1[i] in nums2 and nums1[i] not in s:
                    s.add(nums1[i])
        s = list(s)
        return s
