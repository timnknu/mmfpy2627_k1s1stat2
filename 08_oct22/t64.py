txt = "       hello,     wo rld      !!!   "

s = ''
prev = ' '
for ch in txt:
    if ch != prev or ch != ' ':
        print('we appended:', ch)
        s = s + ch
        prev = ch
if len(s) > 0 and prev == ' ':
    s = s[:-1]

print(f'|{s}|')

