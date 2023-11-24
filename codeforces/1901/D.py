n = int(input())
a = list(map(int, input().split()))

b = [0] * (n)
c = [0] * (n)

l1, l2 = 0, 0
for i in range(n):
    l1 += 1
    if l1 < a[i]:
        l1 = a[i]
    b[i] = l1

for i in range(n - 1, -1, -1):
    l2 += 1
    if l2 < a[i]:
        l2 = a[i]
    c[i] = l2

least = c[0]
for i in range(1, n - 1):
    # print(least)
    least = min(least, max(b[i - 1] + n - i, c[i + 1] + i + 1, a[i]),)
least = min(least, b[-1])
# print(b)
# print(c)
print(least)