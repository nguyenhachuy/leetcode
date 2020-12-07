from collections import Counter
from operator import itemgetter
import heapq
class Solution(object):
    def reorganizeString(self, S):
        N = len(S)
        A = []
        for c, x in sorted((S.count(x), x) for x in set(S)):
            if c > (N+1)/2: return ""
            A.extend(c * x)
        ans = [None] * N
        ans[::2], ans[1::2] = A[N//2:], A[:N//2]
        return "".join(ans)

def main():
    sol = Solution()
    print(sol.reorganizeString("aab"))
    print(sol.reorganizeString("aaab"))
    print(sol.reorganizeString("abcabcabcdaa"))
if __name__ == "__main__":
  main()


"""
a_a_a_...
b_b_b_...
c_c_c_...

"""
