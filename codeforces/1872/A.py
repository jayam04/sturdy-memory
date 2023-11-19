ts = int(input())

for t in range(ts):
    a, b, c = list(map(int, input().split()))
    d = (a - b) / 2
    d = max(d, -d)
    if d % c == 0:
        print(int(d // c))
        continue
    print(int(d // c + 1))
