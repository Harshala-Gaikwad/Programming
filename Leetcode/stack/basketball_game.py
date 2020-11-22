class Solution:
    def calPoints(self, ops: List[str]) -> int:
        result = []
        for i in range(len(ops)):
            if ops[i]=="+":
                result.append(result[-1]+result[-2])
            elif ops[i]=="D":
                result.append(int(result[-1])*2)
            elif ops[i]=="C":
                result.pop()
            else:
                result.append(int(ops[i]))
        sum_ = sum(result)        
        return sum_        
                
        
