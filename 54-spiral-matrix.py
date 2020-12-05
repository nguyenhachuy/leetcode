class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        top,right,bottom,left = 0, n-1, m-1, 0
        result = []
        while top < bottom and left < right:
            result.extend(matrix[top][left:right])
            for i in range(top, bottom):
                result.append(matrix[i][right])
            for i in reversed(range(left+1, right+1)):
                result.append(matrix[bottom][i])
            for i in reversed(range(top+1,bottom+1)):
                result.append(matrix[i][left])
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        
        if top==left==right==bottom:
            result.append(matrix[top][left])
        elif top == bottom:
            result.extend(matrix[top][left:right+1])
        elif left == right:
            for i in range(top, bottom+1):
                result.append(matrix[i][left])
        
        return result