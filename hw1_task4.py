n = int(input("Введите любое целое положительное число="))
a = n % 10
n = n // 10
while n > 0:
    if (n % 10) > a:
        a = n % 10
    n = n // 10
print(a)

