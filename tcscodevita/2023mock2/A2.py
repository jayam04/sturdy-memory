pages = int(input())

edges = {}

for i in range(pages):
    edges[i] = list(map(int, input().split()))
# print(edges)

rechable = [float('inf') for _ in range(pages)]
rechable[0] = 0

queue = []
for node in edges[0]:
    queue.append([0, node - 1])

while queue:
    edge = queue.pop(0)
    rechable[edge[1]] = min(rechable[edge[0]] + 1, rechable[edge[1]])
    nodes = edges[edge[1]]
    for node in nodes:
        queue.append([edge[1], node - 1])
    edges[edge[1]] = []


if rechable[-1] == float('inf'):
    print(-1)
else:
    print(rechable[-1])
