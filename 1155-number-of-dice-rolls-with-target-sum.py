class Solution:
    # top down
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10 ** 9 + 7
        @lru_cache(maxsize=None)
        def dp(d, target):
            if d == 0:
                return 0 if target > 0 else 1
            ways = 0
            for i in range(max(target - f, 0), target):
                ways += dp(d-1, i)
            return ways % mod
        
        return dp(d, target) % mod

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0 for _ in range(target+1)] for _ in range(2)]
        dp[0][0] = 1
        for i in range(1,d+1):
            for j in range(1,target+1):
                dp[1][j] = sum(dp[0][x] for x in range(max(0, j-f), j)) % mod
            dp[0], dp[1] = dp[1], [0 for _ in range(target+1)]
        return dp[0][target]

