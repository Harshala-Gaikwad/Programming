class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ["+","-","*","/"]
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in op:
                stack.append(tokens[i])
            else:
                if tokens[i]=="+":
                    ans = int(stack[-2])+int(stack[-1])
                elif tokens[i]=="-":
                    ans = int(stack[-2])-int(stack[-1])
                elif tokens[i]=="*":
                    ans = int(stack[-2])*int(stack[-1])
                elif tokens[i]=="/":
                     ans = int(int(stack[-2])/int(stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(ans)
        return stack[0]    
