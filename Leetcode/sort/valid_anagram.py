class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''s=sorted(s)
        t = sorted(t)
        if s==t:
            return True
        return False '''
        if len(s)!=len(t):
            return False
        return sorted(s)==sorted(t)
        
