txt = "Hello, all world? Absolutely!"
L = []
for c in txt:
    if c.lower() not in L:
        #if c in 'AEIOUY':
        if c.lower() in 'aeiouy':
            L.append(c.lower())

print('letters:', L)
for ch in L:
    #print(ch, txt.count(ch) + txt.count(ch.upper()))
    print(ch, txt.lower().count(ch))
