class Solution:
    def minOperations(self, logs: List[str]) -> int:
        l = []
        for i in logs:
            if i=="../" and len(l)!=0:
                l.pop()
            elif i!="./" and i!="../":
                l.append(i)
        return len(l)    
