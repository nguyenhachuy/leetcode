import math
from typing import List

class Solution:
    def findMaxSingle(self, num, k):
        st = []
        for i,v in enumerate(num):
            while st and st[-1] < v and (len(st) + len(num) - i) > k:
                st.pop()
            st.append(v)
        return st[:k]
    def merge(self, num1, num2):
        left, right = 0,0
        result = []
        while left < len(num1) and right < len(num2):
            if self.compare(num1, num2, left, right):
                result.append(num1[left])
                left += 1
            else:
                result.append(num2[right])
                right += 1

        if left < len(num1):
            result.extend(num1[left:])
        if right < len(num2):
            result.extend(num2[right:])
        return result
    def compare(self, num1, num2, i, j):
        while i < len(num1) and j < len(num2) and num1[i] == num2[j]:
            i += 1
            j += 1
        return j == len(num2) or (i < len(num1) and num1[i] > num2[j])

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        result = [-math.inf for _ in range(k)]
        for i in range(max(0, k-len(nums2)),min(k+1, len(nums1)+1)):
            num1 = self.findMaxSingle(nums1, i)
            num2 = self.findMaxSingle(nums2, k-i)
            if len(num1) + len(num2) == k:
                combined = self.merge(num1, num2)
                result = combined if self.compare(combined, result, 0, 0) else result
        return result


def main():
  sol = Solution()
  print(sol.maxNumber([9, 1, 2, 5, 8, 3], [3, 4, 6, 5], 5))
  print(sol.maxNumber([6,7], [6,0,4], 5))

if __name__ == "__main__":
  main()

"""
Input:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
Output:
[9, 8, 6, 5, 3]

pick the largest number of both arrays, only on an increasing path (last element). if it's a decreasing path, must pick the first element
answer is a decreasing stack, stack has length k
at each number, i can ignore it if i know there are more larger in the future, and the rest can fit k
[6,5]
[9,8,3]
T(nums1,nums2,k) = max( T(nums1[x:], nums2, k-1) for x in range(len(nums1) - k + len(nums2)), ....)

"""
