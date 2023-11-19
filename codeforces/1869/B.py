def find_route(a, b):
    dx = max(a[0] - b[0], b[0] - a[0])
    dy = max(a[1] - b[1], b[1] - a[1])
    return dx + dy

ts = int(input())

for _ in range(ts):
    n, k, a, b = list(map(int, input().split()))
    a -= 1
    b -= 1

    cities = []
    x = [float('inf'), float('-inf')]
    y = [float('inf'), float('-inf')]
    np1 = float('inf')
    np2 = float('inf')

    for i in range(n):
        cities.append(list(map(int, input().split())))

    for i in range(k):
        tgv = find_route(cities[i], cities[a])
        np1 = min(np1, tgv )
        
        tgv = find_route(cities[i], cities[b])
        np2 = min(np2, tgv)

        x[0] = min(x[0], cities[i][0])
        x[1] = max(x[1], cities[i][0])
        y[0] = min(x[0], cities[i][1])
        y[1] = max(x[0], cities[i][1])
    
    a, b = cities[a], cities[b]
    directx = max(a[0] - b[0], b[0] - a[0])
    directy = max(a[1] - b[1], b[1] - a[1])
    direct = directx + directy
        
    ind = np1 + np2

    print(min(ind, direct))
