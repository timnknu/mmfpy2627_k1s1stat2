txt = "helllo, woooorld!!!"

res = []
# for ch in txt:
#     if len(res) == 0 or ch != res[-1]:
#         res.append(ch)

for i, ch in enumerate(txt):
    if i == 0 or ch != res[-1]:
        res.append(ch)


# s = ''
# for el in res:
#     s = s + el
# print(s)
s = ''.join(res)
print(s)
