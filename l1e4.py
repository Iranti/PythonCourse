a = int(input("Введите положительное число:\n"))
m = 0
while a > 0:
    b = a % 10
    a = a // 10
    if m > b:
        m = m
    else: m = b

print(m)