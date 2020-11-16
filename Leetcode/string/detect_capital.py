class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        flag = 0
        if word.isupper():
            flag = 1
        elif word.islower():
            flag = 1
        elif word[0].isupper() and word[1:].islower():
            flag = 1
        if flag==1:
            return True
        else:
            return False
