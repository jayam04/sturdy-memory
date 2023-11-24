testcases = int(input())

for testcase in range(testcases):
    n, x = list(map(int, input().split()))
    a =  list(map(int, input().split()))
    least = max(2 * (x - a[-1]), a[0])
    for i in range(1, n):
        if a[i] - a[i - 1] > least:
            least = a[i] - a[i - 1]
    print(least)