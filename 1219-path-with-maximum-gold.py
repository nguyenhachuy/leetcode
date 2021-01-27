class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        def backtracking(i,j):
            left = 0
            gold = grid[i][j]
            grid[i][j] = 0
            if (i-1) >= 0 and grid[i-1][j] > 0:
                left = backtracking(i-1,j)
            right = 0
            if (i+1) < m and grid[i+1][j] > 0:
                right = backtracking(i+1,j)
            top = 0
            if (j-1) >= 0 and grid[i][j-1] > 0:
                top = backtracking(i, j-1)
            bottom = 0
            if (j+1) < n and grid[i][j+1] > 0:
                bottom = backtracking(i, j+1)

            grid[i][j] = gold
            return max(left,right,top,bottom) + gold
        max_gold = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    max_gold = max(max_gold, backtracking(i,j))
        return max_gold
"""
sounds like a backtracking problem
dp(i,j) = grid[i][j] + dp(i-1,j), dp(i+1,j), dp(i,j-1), dp(i,j+1)
with the conditino that it's valid path and there's gold
once that ha ppens, replace the gold back
"""
