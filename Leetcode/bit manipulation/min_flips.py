class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        for i in range(32):
            x = y = z = False
            if a&(1<<i): x = True
            if b&(1<<i): y = True
            if c&(1<<i): z = True
            
            if z== False:
                
                if x== True and y== True:
                    res+=2
                elif  x== True or y== True:
                    res+=1 
            else:
                if x== False and y== False:
                    res+=1
        return res            
                    
