class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S1 = ""
        T1 = ""
        for i,x in enumerate(S):
            if x=="#":
                S1 = S1[:-1]
            else:
                S1+=x
        for i,x in enumerate(T):
            if x=="#":
                T1 = T1[:-1]
            else:
                T1+=x
        if S1==T1: return True
        return False
