class Solution:
    def rob(self, nums: List[int]) -> int:
        a,b = 0,0
        for i in reversed(range(len(nums))):
            temp = max(nums[i] + b, a)
            a,b = temp,a
        return a
