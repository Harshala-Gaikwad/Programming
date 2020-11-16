class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = []
        for i in range(m):
            l.append(nums1[i])
        nums1.clear()
        for x in l:
            nums1.append(x)
        nums1.extend(nums2) 
        nums1.sort()
        
