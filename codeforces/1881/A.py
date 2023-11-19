ts = int(input())

def comp(s, x, i):
    for j in range(len(s)):
        if s[j] != x[(i + j) % len(x)]:
            return -1
    return (i + j) // len(x)

for _ in range(ts):
    n, m = list(map(int, input().split()))
    x = input()
    s = input()

    res = 0
    while len(x) < len(s):
        x = x * 2
        res += 1
    
    for i in range(len(x)):
        r = comp(s, x, i)
        if r != -1:
            print(res + r)
            break
    else:
        print(-1)
