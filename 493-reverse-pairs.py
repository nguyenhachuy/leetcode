class BIT:
    def __init__(self, n):
        self.n = n + 1
        self.sums = [0] * self.n

    def update(self, i, delta):
        # Add 1 for offset
        i = i + 1
        while i < self.n:
            self.sums[i] += delta
            i += i & (-i)

    def query(self, i):
        # Add 1 for offset
        i = i + 1
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= i & (-i)
        return res

class Solution:
    def reversePairs(self, nums):
        # Get the relative position of the doubled number compared to the real numbers
        # Make it a set to reduce size because we don't care if we see 1 or many
        doubled = sorted(list(set(nums + [num*2 for num in nums])))
        # Precompute ranks to optimize without binary search
        ranks = {v:i+1 for i,v in enumerate(doubled)}
        tree = BIT(len(doubled))
        result = 0
        for i in reversed(range(len(nums))):
            # At every step, we query all doubled numbers less than nums[i], we -1 to get the previous number instead
            # An alternative is:
            # result += tree.query(bisect.bisect_left(doubled, nums[i])-1)
            # This means find the index of the doubled number <= nums[i], -1 to ensure it's strictly less than
            result += tree.query(ranks[nums[i]]-1)
            # An alternative is:
            # Update the frequency of doubled numbers to the tree
            # tree.update(bisect.bisect_left(doubled, nums[i]*2), 1)
            tree.update(ranks[nums[i]*2], 1)
        return result
