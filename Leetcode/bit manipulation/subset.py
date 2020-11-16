class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(2**len(nums)):
            s = bin(i).replace("0b","")
            if len(s)!=len(nums):
                s = "0"*(len(nums)-len(s))+s
            temp = []
            for i in range(len(s)):
                if s[i] == "1":
                    temp.append(nums[i])
            result.append(temp)
        return result  
