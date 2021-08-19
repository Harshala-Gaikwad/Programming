# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    if y2>=y1:
        if y2==y1:
            if m2<m1:
                return 500*(m1-m2)
            elif m2==m1:
                if d2<d1:
                    return 15*(d1-d2)
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    else:
        return 1000
    


d1M1Y1 = input().split()

d1 = int(d1M1Y1[0])

m1 = int(d1M1Y1[1])

y1 = int(d1M1Y1[2])

d2M2Y2 = input().split()

d2 = int(d2M2Y2[0])

m2 = int(d2M2Y2[1])

y2 = int(d2M2Y2[2])

result = libraryFine(d1, m1, y1, d2, m2, y2)

print(result)
