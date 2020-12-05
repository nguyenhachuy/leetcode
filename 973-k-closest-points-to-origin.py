class Solution:
    def distance(self, a,b):
        return -1*math.sqrt(a**2+b**2)
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for point in points:
            x,y = point
            heapq.heappush(heap, (self.distance(x,y), [x,y]))
            if len(heap) > K:
                heapq.heappop(heap)
        return [x[1] for x in heap]
