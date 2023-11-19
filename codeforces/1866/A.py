n = int(input())
arr = list(map(int, input().split()))

m = max(arr[0], -arr[0])

for i in arr:
    if i > 0:
        m = min(m, i)
    else:
        m = min(m, -i)

print(m)
