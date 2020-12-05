class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(2)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                match = 1 if text1[i-1] == text2[j-1] else 0
                if match:
                    dp[1][j] = 1 + dp[0][j-1]
                else:
                    dp[1][j] = max(dp[0][j], dp[1][j-1], dp[0][j-1])
            dp[0], dp[1] = dp[1], dp[0]
        return dp[0][n]
