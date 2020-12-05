import math
class Solution:
    def sumSubarrayMins(self, A):
        res = 0
        stack = []  #  non-decreasing 
        A = [-math.inf] + A + [-math.inf]
        for i, n in enumerate(A):
            while stack and A[stack[-1]] > n:
                cur = stack.pop()
                # print(cur,stack[-1], stack)
                res += A[cur] * (i - cur) * (cur - stack[-1]) 
            stack.append(i)
        return res % (10**9 + 7)


def main():
  arr = [3,1,2,4]
  sol = Solution()
  print(sol.sumSubarrayMins(arr))

if __name__ == "__main__":
  main()
