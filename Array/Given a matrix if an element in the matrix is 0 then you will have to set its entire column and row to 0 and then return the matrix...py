class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        row = [0] * m
        col = [0] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1

        for i in range(m):
            for j in range(n):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
obj = Solution()
obj.setZeroes(matrix)
for r in matrix:
    print(r)
