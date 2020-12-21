# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
import math
class BinaryMatrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
    def get(self, row: int, col: int):
        return self.matrix[row][col]
    def dimensions(self):
        return [len(self.matrix), len(self.matrix[0])]

class Solution:
    def find_leftmost_zero(self, matrix, row, col_length, starting_col):
        left = 0
        right = starting_col if starting_col < math.inf else col_length-1
        result = math.inf
        if right < left or right < 0:
            return result

        while left <= right:
            mid = left + (right-left)//2
            if matrix.get(row, mid) == 1:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result

    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m,n = binaryMatrix.dimensions()
        leftmost = math.inf
        for i in reversed(range(m)):
            leftmost = min(leftmost, self.find_leftmost_zero(binaryMatrix, i, n, leftmost))
        return leftmost if leftmost < math.inf else -1


def main():
    sol = Solution()
    print(sol.leftMostColumnWithOne(BinaryMatrix([[0,0],[1,1]])))
    print(sol.leftMostColumnWithOne(BinaryMatrix([[0,0],[0,1]])))
    print(sol.leftMostColumnWithOne(BinaryMatrix([[0,0],[0,0]])))
    print(sol.leftMostColumnWithOne(BinaryMatrix([[0,0,0,1],[0,0,1,1],[0,1,1,1]])))
    print(sol.leftMostColumnWithOne(BinaryMatrix([[1,1,1,1,1],[0,0,0,1,1],[0,0,1,1,1],[0,0,0,0,1],[0,0,0,0,0]])))
if __name__ == "__main__":
    main()

"""
BF column by column scan, O(n^2)
how to use sortedness of row?
max dimension: 100x100 = 10000, max call 1000
if check each row, detect whether there's a 1, and then binary search to find the leftmost 1
since each row are not related, we must search each row individually
log(100)
"""
