from typing import List
import math
class Solution:
    def distance(self, pair):
        a,b = pair
        return math.sqrt(a**2+b**2)
    def mergesort(self, points, i, j, k):
        if i == j:
            return [points[i]]
        mid = i + (j-i)//2
        left = self.mergesort(points, i, mid, k)
        right = self.mergesort(points, mid+1, j, k)

        a,b = 0,0
        result = []
        while len(result) < k and a < len(left) and b < len(right):
            if self.distance(left[a]) < self.distance(right[b]):
                result.append(left[a])
                a += 1
            else:
                result.append(right[b])
                b += 1

        while len(result) < k and a < len(left):
            result.append(left[a])
            a += 1
        while len(result) < k and b < len(right):
            result.append(right[b])
            b += 1
        return result

    # def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    #     heap = []
    #     for point in points:
    #         x,y = point
    #         heapq.heappush(heap, (self.distance(x,y), [x,y]))
    #         if len(heap) > K:
    #             heapq.heappop(heap)
    #     return [x[1] for x in heap]

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return self.mergesort(points, 0, len(points)-1, K)

def main():
    sol = Solution()
    print(sol.kClosest([[1,3],[-2,2]], 1))
    print(sol.kClosest([[3,3],[5,-1],[-2,4]], 2))
    print(sol.kClosest([[1,3],[-2,2],[2,-2]], 2))

if __name__ == "__main__":
    main()

