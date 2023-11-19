ts = int(input())

for _ in range(ts):
    x, y, k = list(map(int, input().split()))
    if y <= x:
        print(x)
        continue
    add = x + k
    if add >= y:
        print(y)
        continue
    else:
        print(2 * y - add)
