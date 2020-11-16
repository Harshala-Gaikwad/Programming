class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        max_ = curr = start =0
        for index,i in enumerate(s):
            if i in d and d[i] >= start:
                max_ = max(max_,curr)
                curr = index - d[i]
                start = d[i]+1
            else:
                curr += 1
            d[i] = index
        return max(max_,curr)   
           
