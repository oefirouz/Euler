import math
n = 1000
phi = (math.sqrt(5) + 1)/2.0
print int(round((n-1)/math.log10(phi) + 2))
