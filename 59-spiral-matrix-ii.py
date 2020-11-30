class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        top,bottom = 0, n-1
        left, right = 0, n-1
        count = 1
        while top < bottom:
            for i in range(left, right):
                matrix[top][i] = count
                count += 1
            for i in range(top, bottom):
                matrix[i][right] = count
                count += 1
            for i in reversed(range(left+1, right+1)):
                matrix[bottom][i] = count
                count += 1
            for i in reversed(range(top+1, bottom+1)):
                matrix[i][left] = count
                count += 1
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        
        if top == bottom == left == right:
            matrix[top][bottom] = count

        return matrix
        