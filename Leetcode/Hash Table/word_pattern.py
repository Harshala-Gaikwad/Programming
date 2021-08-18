class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l = s.split()
        if len(pattern) != len(l):
            return False
        
        d = {}
        d1 = {}
        
        for i,j in zip(pattern,l):
            if i not in d:
                d[i]=j
            if j not in d1:
                d1[j]=i
            if d[i]!=j or d1[j]!=i:
                return False
        return True    
        
