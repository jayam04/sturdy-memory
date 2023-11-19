def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

ts = int(input())
for _ in range(ts):
    l, r = list(map(int, input().split()))

    a = 2
    b = max(2, l - 2)

    if a + b > r:
        print(-1)
        continue

    inc = True
    while a <= b:
        if gcd(a, b) != 1:
            print(a, b)
            break
        if inc:
            if a + b < r:
                b += 1
            else:
                inc = False
                a += 1
                b -= 1
        else:
            if a + b > l:
                b -= 1
            else:
                inc = True
                a += 1
                b -= 1
    else:
        print(-1)
