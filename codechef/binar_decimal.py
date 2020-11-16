def DecimalToBinary(num):
    decimal =0
    for i in num:
        decimal = decimal*2 + int(digit)
    print(decimal)    
DecimalToBinary(101)    
def BinaryConcatenation(x,y):
    binX = str(bin(x))
    binX = binX[2:]
    binY = str(bin(y))
    binY = binY[2:]
    binXplusY = binX+binY
    binYplusX = binY+binX
    print(binX,binY,binXplusY)
BinaryConcatenation(5,9)    
