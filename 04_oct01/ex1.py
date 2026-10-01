
is_finished = False

while (not is_finished) :
    x = int(input())
    print('ви ввели', x)
    print('цикл продовжується')
    if x == -1:
        is_finished = True

print('цикл завершився')



# #####
#
#
# should_resume = True
#
# while should_resume:
#     x = int(input())
#     print('ви ввели', x)
#     print('цикл продовжується')
#     if x == -1:
#         should_resume = False
#
# print('цикл завершився')