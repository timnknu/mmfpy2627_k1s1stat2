from typing import cast

cnt = 0

while True :
    x = int(input())
    print('ви ввели', x)
    if x == 0:
        break
    # if x%2 != 0: # x%2 == 1:
    #     print('число непарне')
    #     # отже, число x -- непарне
    #     cnt = cnt + 1   # cnt += 1

    if x%2 == 0: # x%2 != 1:
        # парні елементи нам за умовою НЕ потрібні
        continue

    # отже, число x -- непарне
    print('число непарне')
    cnt = cnt + 1   # cnt += 1

    print('цикл продовжується')

print('цикл завершився')
print(cnt)