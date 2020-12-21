from typing import List
from bisect import bisect_left
class Solution:
    def canCross(self, stones):
        dp = {}
        for stone in stones:
            dp[stone] = set()
        stone_set = set(stones)
        dp[0].add(0)

        for i,v in enumerate(stones):
            for k in dp[v]:
                for step in range(k-1,k+2):
                    if step > 0 and v + step in dp:
                        if v + step == stones[-1]:
                            return True
                        dp[v + step].add(step)

        return False
    # Recursion
    def dp(self, index, prev_jump, stones):
        if index == len(stones) - 1:
            return True
        if index >= len(stones):
            return False

        k_1 = False
        next_stone = stones[index]+prev_jump+1
        for i in range(index+1, len(stones)):
            if stones[i] == next_stone:
                k_1 = self.dp(i, prev_jump+1, stones)
        if prev_jump == 0:
            return k_1
        k_stone = stones[index]+prev_jump
        k = False
        for i in range(index+1, len(stones)):
            if stones[i] == k_stone:
                k = self.dp(i, prev_jump, stones)
        if prev_jump == 1:
            return k or k_1

        prev_k = False
        prev_stone = stones[index]+prev_jump-1
        for i in range(index+1, len(stones)):
            if stones[i] == prev_stone:
                prev_k = self.dp(i, prev_jump-1, stones)

        return k or k_1 or prev_k

    def dp2(self, index, prev_jump, stones, table):
        if index == len(stones) - 1:
            return True
        if index >= len(stones):
            return False
        if (index, prev_jump) in table:
            return table[(index, prev_jump)]
        table[(index, prev_jump)] = False
        next_stone = stones[index]+prev_jump+1
        next_stone_index = bisect_left(stones, next_stone)
        if stones[next_stone_index] == next_stone:
            table[(index, prev_jump)] |= self.dp(next_stone_index, prev_jump+1, stones)
        if prev_jump == 0:
            return table[(index, prev_jump)]
        k_stone = stones[index]+prev_jump
        k_stone_index = bisect_left(stones, k_stone)
        if stones[k_stone_index] == k_stone:
            table[(index, prev_jump)] |= self.dp(k_stone_index, prev_jump, stones)
        if prev_jump == 1:
            return table[(index, prev_jump)]

        prev_stone = stones[index]+prev_jump-1
        prev_stone_index = bisect_left(stones, prev_stone)
        if stones[prev_stone_index] == prev_stone:
            table[(index, prev_jump)] |= self.dp(prev_stone_index, prev_jump-1, stones)

        return table[(index, prev_jump)]

    def canCross(self, stones: List[int]) -> bool:
        table = {}
        return self.dp2(0, 0, stones, table)


def main():
    sol = Solution()
    # sol.schedule_tasks(["A"], ["X", "Y", "Z"])
    # sol.schedule_tasks(["A", "B"], ["X", "Y", "Z"])
    arrays = [[0,1,2,3,4,8,9,11], [0,1,3,5,6,8,12,17], [0], [0,1], [0,1,2], [0,1,8]]
    for array in arrays:
        print(array, ": ", sol.canCross(array))
if __name__ == "__main__":
    main()
