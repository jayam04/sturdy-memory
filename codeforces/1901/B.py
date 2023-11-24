testcases = int(input())

for testcase in range(testcases):
    n = int(input())
    c = list(map(int, input().split()))
    last = 1
    teleports = 0
    for i in c:
        if i > last:
            teleports += i - last
        last = i
    print(teleports)