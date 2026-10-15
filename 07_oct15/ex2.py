# задано текст; знайти, скільки разів в ньому
# зустрічається кожна літера

txt = "він знаходиться на самому початку рядка, до самого першого слова"
# підзадача: з яких літер складається цей текст?
# сформувати список із цих літер
L = []
for c in txt:
    if c not in L:   #if not (c in L):
        #if ...якщо c є саме літерою, а не якимось іншим символом...:
        if c.isalpha():
        # c=='В'  ...c... in 'абв......' -> True
        #if c.lower() in 'абв......':
            L.append(c)
#print(L)
#print(len(L))

for ch in L:
    #print(ch, txt.count(ch))
    ntimes = 0
    for K in txt:
        if K == ch:
            ntimes = ntimes + 1
    print(ch, ntimes, txt.count(ch))



