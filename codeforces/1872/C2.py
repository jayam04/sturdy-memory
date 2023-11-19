ans = []

ts = int(input())
for _ in range(ts):
    l, r = list(map(int, input().split()))
    
    a = 2
    while a < l // 2:
        b = (l // a - 1) * a
        if l % a != 0:
            b += a
        if a + b < r:
            print(a, b)
            ans.append([a, b])
            break
        a += 1
    else:
        print(-1)
        ans.append([-1])

print(ans)
