testcases = int(input())

for testcase in range(testcases):
    t1, t2, t3 = list(map(int, input().split()))

    if t1 > t3:
        t3, t1 = t1, t3
    if t1 > t2:
        t1, t2 = t2, t1
    if t2 > t3:
        t2, t3 = t3, t2

    rem = 3
    if t1 == 1:
        if (t2 + t3 - 2 <= rem):
            print("YES")
        else:
            print("NO")
        continue
    if t2 % t1 != 0 or t3 % t1 != 0:
        print("NO")
        continue
    if (t2 // t1 + t3 // t1 - 2 <= rem):
        print("YES")
    else:
        print("NO")
