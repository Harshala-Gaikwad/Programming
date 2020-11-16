class Solution:
    def countBits(self, num: int) -> List[int]:
        result = []
        for n in range(num+1):
            count = 0
            #n = int(bin(i).replace("0b",""))
            while n>0:
                count+=1
                n = n&(n-1)
            result.append(count)
        return result   
