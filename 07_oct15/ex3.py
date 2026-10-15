txt = 'сьогодні'

print('о' in txt)
print('ї' in txt)
print('ого' in txt)
print('огого' in txt)


print(txt.upper())
print('Сьогодні'.upper())
print('Сьогодні'.lower())

print(list(txt))
print(tuple(txt))

#x = ['he', 'y!']
x = 125
print(x)
K = str(x)
print(K)
print('Результат циклу:')
for ch in K:
    print('елемент:', ch)