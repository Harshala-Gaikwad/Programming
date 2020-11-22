class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        for i in arr2:
            x = arr1.count(i)
            for j in range(x):
                result.append(i)
                arr1.remove(i)
        arr1.sort()        
        for i in arr1:
            result.append(i)
        return result        
        
