x = 0.9

s = 0
for n in range(100):
    s = s + x**n

print(s)
print(1/(1-x))