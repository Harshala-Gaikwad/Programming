class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        curr = prev = total=0
        for i in s:
            curr = d[i]
            if curr>prev:
                total+=curr-2*prev
            else:
                total+=curr
            prev = curr    
        return total        
            
        
