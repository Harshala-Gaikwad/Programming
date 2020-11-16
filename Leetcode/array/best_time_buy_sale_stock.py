class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0: return 0
        ans,min_ = 0,prices[0]
        for i in range(1,len(prices)):
            if prices[i]<min_:
                min_ = prices[i]
            else:
                ans = max(ans,prices[i]-min_)
        return ans         
        
