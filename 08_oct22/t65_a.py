txt = "helllo, woooorld!!!"

s = ''
prev = ''
for ch in txt:
    if ch != prev:
        print('we appended:', ch)
        s = s + ch
        prev = ch

print(s)
