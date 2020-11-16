class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1:
            return False
        open_brackets = ['[','(','{']
        close_brackets = [']',')','}']
        result = []
        for i in s:
            if i in open_brackets:
                result.append(i)
            elif i in close_brackets:
                pos = close_brackets.index(i)
                if len(result)>0:
                    if result[len(result)-1]==open_brackets[pos]:
                        result.pop()
                    else:
                        return False
                else:
                    return False
        if len(result)==0:
            return True
        else:
            return False
