import math
a = int(input())
b = int(input())
c = int(input())
d = b**2-4*a*c
s = math.sqrt(d)
x1 = (-b+s)/(2*a)
x2 = (-b-s)/(2*a)
print(x1)
print(x2)
