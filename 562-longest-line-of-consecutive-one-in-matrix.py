class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        max_length = 0
        if not M:
            return 0
        m,n = len(M), len(M[0])
        dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(4)]
        for i in range(m):
            for j in range(n):
                if M[i][j] == 1:
                    dp[0][i][j] = dp[0][i][j-1] + 1 if j-1 >= 0 else 1
                    dp[1][i][j] = dp[1][i-1][j] + 1 if i-1 >= 0 else 1
                    dp[2][i][j] = dp[2][i-1][j-1] + 1 if (i-1 >= 0 and j-1 >= 0) else 1
                    dp[3][i][j] = dp[3][i-1][j+1] + 1 if (i-1 >= 0 and j+1 < n) else 1
                    max_length = max(max_length, max(dp[x][i][j] for x in range(4)))
        return max_length

"""
once we find a longest line, other lines must be at least longer than that
sliding window vertical, horizontal, diagonal, anti-diagonal
if encounter a 0, break
and move left bound to after that 0, or the next available 1 because
any line starting before that will always be smaller than the one we already find
3d dp
dp(i,j,direction) = 0 if current number is 0
1 if previous opposite of direction is out of bound
1 + previous opposite. direction if it it is valid

max it out
"""
