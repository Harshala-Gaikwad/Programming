def timeConversion(s):
    #
    # Write your code here.
    #
    if s[0:2]=='12' and s[8:]=='AM':
        s='00'+s[2:8]
    elif s[8:]=='PM'and s[0:2]!='12':
        s=str(int(s[0:2])+12)+s[2:8]
    return s    


s = input()
result = timeConversion(s)
print(result)
