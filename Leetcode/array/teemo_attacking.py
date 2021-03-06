class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries)==0: return 0
        total = 0
        for x in range(len(timeSeries)-1):
            total += min(timeSeries[x+1]-timeSeries[x],duration)
        return total+duration    
 
