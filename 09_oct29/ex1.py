import math

def arcoth(x):
    y = 0.5 * math.log((x+1)/(x-1))
    return y

myvar = 2.5
res = arcoth(myvar)
print(res)