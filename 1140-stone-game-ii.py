"""
T(x, m)
T(x[prev_x:], max(prev_M,prev_X))
maximize alice's stone while minimizing bob's stone (if bob starts next)

[2,7,9,4,4]
2 -> call bob, then call alice again. 
we can also sum up all the stones 
so let's say 
take 2, next is sum - (7+9) = 8
take 2,7 next is sum - (7+9+4+4) = 0
and we choose the max between these
here the recurrence relation is:
T(x,m) = max(x[:i] + sum - T(x[i:], max(i,m)) for i in range(1,2*m+1))
sum here is 
"""

import itertools
import math

class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        suffix_sum = list(itertools.accumulate(reversed(piles)))[::-1]
        dp = [[0] * (len(piles)+1) for _ in range(len(piles)+1)]
        for i in reversed(range(len(piles))):
            maxM = math.ceil(len(piles) - i / 2)
            for j in range(1, maxM):
                for k in range(1, min(2*j+1, len(piles)-i+1)):
                    dp[i][j] = max(dp[i][j], suffix_sum[i] - dp[i+k][max(j,k)])

        return dp[0][1]

"""
prefix_sum = [2,9,18,22,26]

i 0
m 1
left 0
result = -math.inf,
  i 1
  m 1
  result = -math.inf
    i 2
    m 1 
    result = -math.inf
    ....

"""

def main():
  piles = [2,7,9,4,4]
  sol = Solution()
  print(sol.stoneGameII(piles))
  # print(sol.stoneGameII([1,2,3,4,5,100]))

if __name__ == "__main__":
  main()