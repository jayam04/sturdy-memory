ts = int(input())

for t in range(ts):
    n = int(input())

    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    
    arr.sort()

    for ar in arr:
        ar.append(int((ar[1] - 1) / 2))

    i = 0
    possible = float('inf')

    while i < len(arr):
        if arr[i][0] > possible:
            break
        else:
            possible = min(possible, arr[i][0] + arr[i][2])
            i += 1
    print(int(possible))
