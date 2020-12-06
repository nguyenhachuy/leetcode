class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest_so_far = 0
        for i in range(len(nums)):
            furthest_so_far = max(furthest_so_far, i + nums[i])
            if furthest_so_far <= i:
                break
        return furthest_so_far >= len(nums) - 1
