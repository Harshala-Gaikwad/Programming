class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        def shiftCount(AA,BB):
            n,count = len(AA),0
            for x in range(n):
                for y in range(n):
                    temp = 0
                    for i in range(y,n):
                        for j in range(x,n):
                            if AA[i][j]==1 and BB[i-y][j-x]==1: temp+=1
                    count = max(count,temp) 
            return count
        return max(shiftCount(A,B),shiftCount(B,A))
        
