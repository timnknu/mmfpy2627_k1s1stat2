# Програма зчитує двоцифрове число і виводить через пропуск кожну цифру окремо

uservalue = input("Введіть двоцифрове число ")
x = int(uservalue)
right_digit = x % 10
y = x // 10
left_digit = y

print(left_digit, right_digit)
#print(f"{left_digit + 10000} nnnn {right_digit}")
print(f"{left_digit} {right_digit}")
