for _ in range(int(input())):
    c = int(input())
    l = len(bin(c).replace('0b',''))
    max_ = 0*(0^c)
    for i in range(1,2**l):
        if i*(i^c) > max_:
            max_ = i*(i^c)
    print(max_)        
  
