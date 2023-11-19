def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)
ts = int(input())
for _ in range(ts):
    n, x, y = list(map(int, input().split()))

    b = n // lcm(x, y)
    h = n // x - b
    l = n // y - b
    print((n * (n + 1) // 2) - ((n - h) * (n - h + 1) // 2) - l * (l + 1) // 2)
