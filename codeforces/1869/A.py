ts = int(input())

for _ in range(ts):
    n = int(input())
    arr = list(map(int, input().split()))

    ops = []

    if n % 2 == 0:
        ops.append([1, n])
        ops.append([1, n])
    
    else:
        ops.append([1, n])
        ops.append([2, n])
        ops.append([1, 2])
        ops.append([1, 2])
    
    print(len(ops))
    for op in ops:
        print(op[0], op[1])
