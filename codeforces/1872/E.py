ts = int(input())
for _ in range(ts):
    some = ""
    n = int(input())
    arr = list(map(int, input().split()))
    ls = input()
    s = []
    xOR = [0, 0]

    i = 0
    for char in ls:
        s.append(char == '1')
        if s[-1]:
            xOR[1] ^= arr[i]
        else:
            xOR[0] ^= arr[i]
        i += 1
    q = int(input())

    for query in range(q):
        arr2 = list(map(int, input().split()))
        if arr2[0] == 1:
            r = 0
            for i in range(arr2[1] - 1, arr2[2]):
                s[i] = not s[i]
                r ^= arr[i]
            xOR[0] ^= r
            xOR[1] ^= r
        else:
            some += str(xOR[arr2[1]]) + " "
    print(some)

