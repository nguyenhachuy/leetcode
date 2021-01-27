from typing import List
from operator import itemgetter

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[1], -x[0]))
        # sort by end time first, interval that ends first dictates the number of points
        # then, intervals that start last is the next condition
        result = 0
        points = None
        for x,y in intervals:
            if not points or x > points[1]:
                result += 2
                points = [y-1,y]
            elif x > points[0]:
                result += 1
                points = [points[1], y]
        return result

"""
return size of set S such that S AND interval always have size at least 2

2 intervals share the same set if those 2 fit in the next interval
if 2 intervals are disjoint, we automatically add 2 more points

given the last interval, the next one has 3 options:
1. overlap > 2 points, pick the last 2 points closest to the edge to maximize upcoming chance of hitting again
2. overlap == 1 point, pick 1 more from the new set, with the point closes to the edge to maximize chance of hitting again
3. not overlap, easy +2

sort by start time, end time => picking end time will most likely work, since we're not constructing, we don't really caare about
which one to pick, as long as the 2 intervals are overlapping


[[1,3],[1,4],[2,5],[3,5]]
2,2,2,2
3,3,3,3+1

the points being considered is held back by the smallest b. once the a of an interval is >= b, we need more than that

[[1,2],[2,3],[2,4],[4,5]]
2,3,3,5

so keep track of minimum_b, use this as the interval check, once past or ==, replace with new interval point.
[[0,7],[1,15],[6,21],[10,21],[15,20]]
[[2,8],[10,23],[11,24],[12,25],[14,25]]

7,8,x,23,
"""

sol = Solution()
test_cases = [
[[1,3],[2,5],[3,5],[1,4]], #3
[[1,2],[2,3],[2,4],[4,5]], #5
[[1,2],[3,4],[5,6]], #6
[[5,10], [2,3], [1,2],[2,5],[3,4],[100,109]], #8
[[2,10],[3,7],[3,15],[4,11],[6,12],[6,16],[7,8],[7,11],[7,15],[11,12]], #5
[[1,3],[3,7],[5,7],[7,8]], #5
[[6,21],[1,15],[15,20],[10,21],[0,7]], #4
[[11,24],[12,25],[2,8],[14,25],[10,23]] #4
]
for t in test_cases:
    print(t, sol.intersectionSizeTwo(t))
