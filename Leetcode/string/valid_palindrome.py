class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for i in s:
            if i.isalnum():
                s1+=i
        s1 = s1.lower()
        s1 = s1.replace(" ","")
        s2 = s1[::-1]
        if s1==s2:
            return True
        else:
            return False
