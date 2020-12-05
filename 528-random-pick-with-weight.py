from operator import itemgetter
import random
class Solution:

    def __init__(self, w: List[int]):
        self.probs = []
        sum_w = sum(w)
        prev_prob = 0
        for i,v in enumerate(w):
            self.probs.append((prev_prob + v/sum_w, i))
            prev_prob += v/sum_w
        self.probs = sorted(self.probs, key=itemgetter(0))

    def binary_search(self, target):
        left, right = 0, len(self.probs)
        while left <= right:
            mid = left + (right -left) // 2
            if self.probs[mid][0] == target:
                return self.probs[mid][1]
            elif self.probs[mid][0] < target:
                left = mid + 1
            else:
                if mid == 0:
                    return self.probs[mid][1]
                elif self.probs[mid-1][0] < target:
                    return self.probs[mid][1]
                else:
                    right = mid - 1
        
        return -1
    def pickIndex(self) -> int:
        random_num = random.uniform(0,1)
        return self.binary_search(random_num)

