txt = "12 + 5 - 11 * 2 * 3 * 4 + 0"
L = []
for c in txt:
    if c not in L:   #if not (c in L):
        if c in ['*', '-', '+']:
        #if c in '*-+':
            L.append(c)

for ch in L:
    print(ch, txt.count(ch))



