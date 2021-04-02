for _ in range(int(input())):
    n = int(input())
    s = input()
    f = ""
    j,k = 4,0
    if n%4==0:
        for i in range(n//4):
            temp = s[k:j]
            bin_int = int(('0b'+temp),2)
            f+=chr(97+bin_int)
            k = j
            j+=4
        print(f)    
        
        
