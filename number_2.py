n = int(input())
sum = 0
if 1 <= n <= 2000:
    for i in range(n):
        b = (n-i)*i
        sum += b
else:
    print('Неверное значение')
print(sum+n)

