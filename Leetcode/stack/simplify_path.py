class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        s1 = path.split("/")
        for i in s1:
            if len(i)>0:
                if i=="..":
                    stack = stack[:-1]
                    #stack.pop()
                elif i!=".":
                    stack.append(i)
        return "/"+"/".join(stack)   
