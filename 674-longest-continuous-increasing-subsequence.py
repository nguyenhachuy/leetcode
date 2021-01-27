class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        i = 0
        max_length = 0
        for j in range(1, len(nums)+1):
            if j-1 == 0 or nums[j-1] > nums[j-2]:
                max_length = max(max_length, j-i)
            else:
                i = j-1

        return max_length
