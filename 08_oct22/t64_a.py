txt = "       hello,     wo rld      !!!   "

L = txt.split()
print(L)

s = ' '.join(L)
print(f'|{s}|')


s = ' '.join(txt.split())
print(f'|{s}|')