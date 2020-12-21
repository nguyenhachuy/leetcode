class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        return max(self.rob_simple(nums, 0, len(nums)-1), self.rob_simple(nums, 1, len(nums)))

    def rob_simple(self, nums: List[int], i, j) -> int:
        t1 = 0
        t2 = 0
        for k in reversed(range(i,j)):
            temp = t1
            t1 = max(nums[k] + t2, t1)
            t2 = temp

        return t1
