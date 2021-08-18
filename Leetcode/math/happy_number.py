class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_(n):
            total = 0
            while n:
                total+=(n%10)**2
                n = n//10
            return total    
            
        while n!=1 and n!=4:
            n = sum_(n)
        if n==1:
            return True
        elif n==4:
            return False
                
                
        
