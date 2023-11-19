testcases = int(input())

for testcase in range(testcases):
    matrixSize = int(input())
    matrix = []
    for i in range(matrixSize):
        matrix.append([c for c in input()])

    req = 0
    for i in range(matrixSize // 2):
        for j in range(i, matrixSize - 1 - i):
            a, b, c, d = matrix[i][j], matrix[j][matrixSize - 1 - i], matrix[-1 -i][-1 -j], matrix[-j - 1][i]
            mina = max(a, b, c, d)
            for char in [a, b, c, d]:
                req += ord(mina) - ord(char)
            # print(mina, req)
    print(req)
