from typing import List
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def find_kth():
            def partition(left, right, i):
                v = nums[i]
                new_pivot_idx = left
                nums[i], nums[right] = nums[right], v
                for j in range(left, right):
                    if nums[j] > v:
                        A[j], A[new_pivot_idx] = A[new_pivot_idx], A[j]
                        new_pivot_idx += 1
                return new_pivot_idx

            left, right = 0, len(nums) - 1
            while left <= right:
                pivot_idx = random.randint(left,right)
                new_pivot_idx = partition(left,right,pivot_idx)
                if new_pivot_idx == k-1:
                    return nums[new_pivot_idx]
                elif new_pivot_idx > k-1:
                    right = new_pivot_idx - 1
                else:
                    left = new_pivot_idx + 1
        return find_kth()

"""
brute force -> sort, n[-k] O(nlogn)
or repeatedly recursion: O(n*k) -> O(n^2)
looking for something like O(n)?

k largest, or n-k smallest
processed + len(st) == k -> answer

either sort, or use a k-heap =.=
"""
