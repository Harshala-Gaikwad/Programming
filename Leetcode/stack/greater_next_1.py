class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        
        stack = []
        for n in nums2:
            while stack and n > stack[-1]:
                next_greater[stack.pop()] = n
            stack.append(n)
            
        while stack:    
            next_greater[stack.pop()] = -1
            
        return [next_greater[n] for n in nums1]
        
