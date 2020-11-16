class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        n = len(A)
        ans = [0]*n
        t=0
        for i,x in enumerate(A):
            if x%2==0:
                ans[t] = x
                t+=2
        t = 1
        for i,x in enumerate(A):
            if x%2!=0:
                ans[t] = x
                t+=2
        return ans   
