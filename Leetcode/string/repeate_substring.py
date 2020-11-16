class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        result = ""
        n = len(s)
        for i in range(n//2):
            result+=s[i]
            if n%len(result)==0:
                if result*(n//len(result))==s:
                    return True
        return False         
            
