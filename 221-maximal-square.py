class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix), len(matrix[0])
        max_square = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    matrix[i][j] = 0
                    continue
                top = int(matrix[i-1][j]) if i-1 >= 0 else 0
                top_left = int(matrix[i-1][j-1]) if (i-1 >= 0 and j-1 >= 0)  else 0
                left = int(matrix[i][j-1]) if j-1 >= 0 else 0
                matrix[i][j] = 1 + min(top, top_left, left)
                max_square = max(max_square, matrix[i][j])
        
        return max_square ** 2
