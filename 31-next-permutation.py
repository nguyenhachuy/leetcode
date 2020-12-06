from typing import List
import math
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        candidate = len(nums) - 2
        while candidate >= 0 and nums[candidate] >= nums[candidate+1]:
            candidate -= 1

        # All increasing
        if candidate == -1:
            left, right = 0, len(nums)-1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            return nums


        to_swap = len(nums) - 1
        while to_swap > candidate:
            if nums[to_swap] > nums[candidate]:
                nums[to_swap], nums[candidate] = nums[candidate], nums[to_swap]
                break
            to_swap -= 1

        left, right = candidate + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums
"""
a < b when a[i] < b[i] for smallest i possible
a is largest when it's a decreasing series all the way
if it's a decreasing series, always take the next larger number in that series, and put that at the earliest spot possible (next to larger number)
the rest order in increasing (or swap)
"""
def main():
    sol = Solution()
    print(sol.nextPermutation([1,2,3]))
    print(sol.nextPermutation([3,2,1]))
    print(sol.nextPermutation([1,1,5]))
    print(sol.nextPermutation([5,4,3,6]))
    print(sol.nextPermutation([8,7,4,5,6]))
    print(sol.nextPermutation([1,3,2]))
if __name__ == "__main__":
  main()
