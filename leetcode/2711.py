class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        def topLeft(r, c):
            r1, c1 = r - 1, c - 1
            distinct = []
            while r1 >= 0 and c1 >= 0:
                distinct.append(grid[r1][c1])
                r1 -= 1
                c1 -= 1
            distinct = set(distinct)
            return len(distinct)
        def bottomRight(r, c):
            r1, c1 = r + 1, c + 1
            distinct = []
            while r1 < len(grid) and c1 < len(grid[0]):
                distinct.append(grid[r1][c1])
                r1 += 1
                c1 += 1
            distinct = set(distinct)
            return len(distinct)
        grid2 = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                t = topLeft(i, j)
                b = bottomRight(i, j)
                if t > b:
                    grid2[i][j] = (t -b)
                else:
                    grid2[i][j] = (b - t)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = grid2[i][j]
        return grid