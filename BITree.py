from collections import defaultdict
from typing import List

"""
https://www.topcoder.com/community/competitive-programming/tutorials/binary-indexed-trees/#read
https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/
"""

class BITree:
  class BITNode:
  def __init__(self, arr):
    self.tree = [0] * (len(arr) + 1)
    self.arr = arr
    for i, v in enumerate(arr):
      self.update(i, v)

  def update(self, index, val):
    index += 1
    while index <= len(self.arr):
      self.tree[index] += val
      index = index + (index & -index)

  def read_cumulative(self, index):
    result = 0
    index += 1
    while index > 0:
      result += self.tree[index]
      index = index - (index & -index)
    return result

  def read_single(self, index):
    index += 1
    return self.arr[index]

  def read_range(self, left, right):
    return self.read_cumulative(right) - self.read_cumulative(left - 1)


def main():
  arr = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]
  tree = BITree(arr)
  for i in range(len(arr)):
    for j in range(i,len(arr)):
      print(f"sum{i}->{j}: ", tree.read_range(i,j))


if __name__ == "__main__":
  main()
