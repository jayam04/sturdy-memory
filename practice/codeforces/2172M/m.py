from collections import deque

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    connects = [[] for _ in range(n + 1)]

    for _ in range(m):
        x, y = map(int, input().split())
        connects[x].append(y)
        connects[y].append(x)

    # BFS shortest paths from node 1
    from_one = [10**18] * (n + 1)
    from_one[1] = 0

    q = deque([1])
    while q:
        u = q.popleft()
        for v in connects[u]:
            if from_one[v] > from_one[u] + 1:
                from_one[v] = from_one[u] + 1
                q.append(v)

    # Build the result for each type (1..k)
    res = [0] * k
    for i in range(1, n + 1):
        t = a[i - 1] - 1
        res[t] = max(res[t], from_one[i])

    print(*res)


main()
