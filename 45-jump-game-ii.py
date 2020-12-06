from typing import List
import math
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        jumps = 1
        max_reachable_position = nums[0]
        max_position_current_index = nums[0]
        for i in range(len(nums)):
            if max_position_current_index < i:
                jump += 1
                max_position_current_index = max_reachable_position
            max_reachable_position = max(max_reachable_position, i+nums[i])

        return jumps


"""
3:40
1 <= nums.length <= 30000
0 <= nums[i] <= 100000


Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

minimum, array => probably dp
subproblem: T(i,arr[i]) = 1 + min(T(i+x, arr[i+x]) for x in range(1, min(arr[i], len(arr) - i))
answer T(0, arr[0])

2d dp: len arr, step size
start from bottom right, move up to top left.
base case: invalid = math.inf
if at last index: 0

T(i=0) = 1 + min(T(i=1),T(i=2))
    T(i=1) = 1 + min(T(i=2), T(i=3), T(i=4))
        T(i=4) = 0
        T(i=3) = 1 + 0 = 1
        T(i=2) = 1 + 1 + 0 = 2
        T(i=1) = 1 + min(2,1,0) = 1
T(i=0) = 1 + 1 = 2
O(m*max_step)=  O(100000*30000) quite large
[2,5,1,1,1]

general approach: use jump game 1, get the concept of maximum reachable position as we go through each index
for every jump, we try to go as far as we can, until we go outside of the range, and we also know the maximum reachable position is always
larger than the max range for the current step, we can replace the max range current step with max reachable position.
however, that requires jumping to that position, and since we just passed outside of the range, the maximum reachable position's index must be
reachable for 1 extra jump.

"""
