class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = set()
        l = []
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                l.append(i)
        return l        
        
