import math
a, b, C = map(int, input().split())
S = a * b * math.sin(math.radians(C)) / 2
L = a + b + math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(C)))
h = b * math.sin(math.radians(C))
print(round(S, 8))
print(round(L, 8))
print(round(h, 8))
