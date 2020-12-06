from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

"""
brute force -> sort, n[-k] O(nlogn)
or repeatedly recursion: O(n*k) -> O(n^2)
looking for something like O(n)?

k largest, or n-k smallest
processed + len(st) == k -> answer

either sort, or use a k-heap =.=
"""
