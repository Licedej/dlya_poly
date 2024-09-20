import math


r = float(input())
print(round(math.pi*r*2, 2))
print(round(math.pi*r**2, 2))


x, y = 10, 55
print(x, y)
x, y = y, x
print(x, y)


l = float(input())
print(round(2*math.pi*((l/9.81)**0.5), 2))
