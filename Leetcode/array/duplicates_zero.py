class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l = []
        i = 0
        n = len(arr)
        while(i!=len(arr) and len(l)!=len(arr)):
            l.append(arr[i])
            if arr[i]==0: l.append(0)
            i+=1 
        arr.clear()
        for i in range(n):
            arr.append(l[i])
               
   
