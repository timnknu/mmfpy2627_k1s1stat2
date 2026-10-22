txt = ", hello,,, world !!!,,"

def myfunc(txt):
    s = ''
    SEP = ','
    prev = SEP
    for ch in txt:
        if ch != prev or ch != SEP:
            s = s + ch
            prev = ch
    if len(s) > 0 and prev == SEP:
        s = s[:-1]
    return s

s = myfunc(txt)
print(f'|{s}|')

