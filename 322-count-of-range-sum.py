import itertools
import bisect
from typing import List
class BITree:
  def __init__(self, length):
    self.tree = [0] * (length + 1)

  def update(self, index, val):
    index += 1
    while index < len(self.tree):
      self.tree[index] += val
      index = index + (index & -index)

  def read(self, index):
    index += 1
    result = 0
    while index > 0:
      result += self.tree[index]
      index = index - (index & -index)
    return result

class Solution:
  def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
    """
    if single element, += to result if inside bounds
    then, form suffix on left partitino and prefix on right partition.
    sort the right partition prefix, binary search twice to find range
    add that range to result
    return the unsorted arrays
    """
    # return self.mergesort(nums, 0, len(nums)-1, lower, upper)
    min_val = min(nums)
    max_val = max(nums)
    tree = BITree(min_val - max_val + 1)

    for i in range(nums):
      for cum_sum in itertools.accumulate(reversed(nums[:i])):
        shifted_sum = cum_sum + nums[i] - min_val
  def mergesort(self, nums, left, right, lower, upper) -> int:
    if left == right:
      return 1 if lower <= nums[left] <= upper else 0
    mid = left + (right-left) // 2
    count = self.mergesort(nums, left, mid, lower, upper) + self.mergesort(nums, mid+1,right, lower, upper)
    suffix = list(itertools.accumulate(reversed(nums[left:mid+1])))
    prefix = list(itertools.accumulate(nums[mid+1:right+1]))
    prefix = sorted(prefix)
    for e in suffix:
      new_lower = lower - e
      new_upper = upper - e
      lower_bound = bisect.bisect_left(prefix, new_lower)
      upper_bound = bisect.bisect(prefix, new_upper)
      count += (upper_bound-lower_bound)
    return count



"""
[-2,5-1]
lower = -2, upper = 2

left 0
right 2
mid = 1
count = 1 + 1 + 1(merge) = 3
suffix = [5,3]
prefix = [-1]
new_lower = -7,-5
new_upper = -3,-1
lower_bound = 0, 0
upper_bound = 0, 1


  left 0
  right 1
  mid 0
  count = 1 + 0 + 0 (merge) = 1
  prefix = [-2]
  suffix = [5]
  new_lower = -2 - 5 = -7
  new_upper = 2 - 5 = -3
  lower_bound = 0
  upper_bound = 0

    left 0
    right 0
    nums[0] = -2, lower <= -2 <= 2
    count = 1

    left 1
    right 1
    nums[1] = 5, not in bounds
    count = 0

  left 2
  right 2
  nums[2] = -1, in bounds
  count = 1

return 2
"""





def main():
  arr = [-2,5,-1]
  sol = Solution()
  print(sol.countRangeSum(arr, -2, 5))

if __name__ == "__main__":
  main()
