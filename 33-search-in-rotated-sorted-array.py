from typing import List

class Solution:
    def binary_search(self, nums, i, j, target):
        while i <= j:
            mid = i + (j-i)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] <= nums[j]:
                if nums[mid] < target <= nums[j]: # pivot is to the left
                    i = mid + 1
                else:
                    j = mid - 1
            else:
                if nums[i] <= target < nums[mid]: # pivot is to the right
                    j = mid - 1
                else:
                    i = mid + 1

        return -1

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums,0,len(nums)-1,target)
"""
[4,5,6,7,0,1,2]
All values of nums are unique.
nums is guranteed to be rotated at some pivot.

drop identifies the pivot -> nums[i+1] < nums[i]
2 binary search on 2 partitions
if there's 1 element, edge case and return whether the element matches
if pivot is 0, there is only 1 partition and we can do binary search in the whole thing.
finding pivot is O(n) + 2 binary search O(2logn)

[5,6,1,2,3,4]
[4,5,6,7,8,1,2,3]
8
"""

def main():
    sol = Solution()
    for i in range(10):
        print(i, sol.search([4,5,6,7,0,1,2], i))
    print(0, sol.search([1], 0))
    print(1, sol.search([1], 1))
    print(5, sol.search([5,1,3], 5))
    print(8, sol.search([4,5,6,7,8,1,2,3], 8))
if __name__ == "__main__":
  main()

