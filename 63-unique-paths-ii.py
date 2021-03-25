from typing import List
"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        dp = [[0 for _ in range(n)] for _ in range(2)]
        dp[0][0] = 1 - obstacleGrid[0][0]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    top = dp[0][j]
                    left = 0 if j-1 < 0 else dp[1][j-1]
                    dp[1][j] = top + left
            dp[0], dp[1] = dp[1], [0 for _ in range(n)]
        return dp[0][n-1]

