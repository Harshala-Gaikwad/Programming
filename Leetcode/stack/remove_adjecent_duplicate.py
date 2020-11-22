class Solution:
    def removeDuplicates(self, S: str) -> str:
        result = []
        for i in S:
            if result and result[-1]==i: result.pop()
            else: result.append(i)
        return "".join(result)    
        
