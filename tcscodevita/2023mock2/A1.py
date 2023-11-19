from pprint import pprint

pages = int(input())

edges = []
from0 = [float("inf") for _ in range(pages)]
from0[0] = 0

# matrix = [[0 for _ in range(pages)] for _ in range(pages)]
# rechable = [[-1 for _ in range(pages)] for _ in range(pages)]

# rechable[0][0] = 0
# pprint(matrix)
for i in range(pages):
    inpt = list(map(int, input().split(" ")))
    for inp in inpt:
        edges.append((i, inp - 1))
        # matrix[i][inp - 1] = 1

edges.sort()
pprint(edges)

queue = [edges[0]]

while queue:
    edge = queue.pop(0)

# for edge in edges:
#     if from0[edge[1]] == 0:
#         continue
#     if from0[edge[0]] != -1:
#         from0[edge[1]] = min(from0[edge[0]] + 1, from0[edge[1]])
#     print(from0)

print(from0)
print(from0[-1])