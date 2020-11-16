class Solution:
    def countAndSay(self, n: int) -> str:
        a = "1"
        for i in range(1,n):
            b = ""
            count = 0
            j = count
            for k in range(len(a)):
                if a[j]==a[k]:
                    count+=1
                else:
                    b+=str(count)+str(a[j])
                    j = k
                    count = 1
            a = b + str(count)+str(a[j])        
        return a            
        
