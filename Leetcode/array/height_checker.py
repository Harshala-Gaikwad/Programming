class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        sort = sorted(heights)
        for index,val in enumerate(sort):
            if sort[index]!=heights[index]:
                count+=1
        return count        
        
