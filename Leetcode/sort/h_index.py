class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        citations.sort()
        h_index = 0
        n = len(citations)
        for i in range(n):
            t_index = n-i
            if citations[i]>=t_index and (i<1 or citations[i-1]<=t_index):
                h_index = max(h_index,t_index)
        return h_index        
        
