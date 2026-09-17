myvar = 15

res = myvar > 1
other = myvar < 2

# res = False
# other = False

print(res, other)

print('-----')

print(res or other)   # логічне "або"
print(res and other)  # логічне "та"
print(not res)       # заперечення
print(not other)     # заперечення


# print((res or other) and (not res) or True)

#print((myvar > 1) or (myvar < 2))   # логічне "або"
