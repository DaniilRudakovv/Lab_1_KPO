num = int(input())
n = list(map(int, str(num)))
total = 0
while int(num) > 9:
    total += 1
    n = list(map(str, str(sum(n))))
    num = ''.join(n)
    n = list(map(int, n))
print(total)