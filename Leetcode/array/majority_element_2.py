class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        limit = n//3
        s = set(nums)
        result = []
        for i in s:
            if nums.count(i)>limit:
                result.append(i)
        return result   
