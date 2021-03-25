class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(2)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                top = dp[0][j]
                left = 0 if j-1 < 0 else dp[1][j-1]
                dp[1][j] = top + left
            dp[0], dp[1] = dp[1], dp[0]
        return dp[0][n-1]

def main():
    sol = Solution()
    cases = [[3,7],[3,2],[7,3],[3,3]]
    for m,n in cases:
        print(m,n, sol.uniquePaths(m,n))

if __name__ == "__main__":
    main()
