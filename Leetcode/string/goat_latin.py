class Solution:
    def toGoatLatin(self, S: str) -> str:
        l = S.split()
        l1 = []
        v = ['a','e','i','o','u','A','E','I','O','U']
        j = 1
        for i in l:
            if i[0] not in v:
                i = i[1:]+i[0]
            i=i + 'ma'+('a')*j
            j+=1
            l1.append(i)

        return(" ".join(l1))
