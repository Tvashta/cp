import math
x, y = map(int, input().split())
print(math.floor(math.log10(x/y)/math.log10(2/3))+1)
