cnt = 0

while True :
    x = int(input())
    print('ви ввели', x)
    if x == 0:
        break

    cnt = cnt + 1   # cnt += 1
    print('цикл продовжується')

print('цикл завершився')
print(cnt)