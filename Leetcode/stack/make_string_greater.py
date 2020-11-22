class Solution:
    def makeGood(self, s: str) -> str:
        '''result = []
        for i in s:
            if i.isupper() and len(result)!=0 and result[len(result)-1]==i.lower():
                result.pop()
            elif i.islower()and len(result)!=0 and result[len(result)-1]==i.upper():
                result.pop()
            else:
                result.append(i)
        return "".join(result) '''
        
        ans = []
        for i in s:
            if ans and i==ans[-1].swapcase(): ans.pop()
            else: ans.append(i)
        return "".join(ans)        
        
