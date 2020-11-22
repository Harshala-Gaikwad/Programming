class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack=[]
        s = ""
        s1 = ""
        for i in S:
            s+=i
            if i=="(": stack.append("(")
            if i==")":stack.pop()   
            if len(stack)==0:
                s1 += s[1:len(s)-1]
                s = ""
        return s1         
        
