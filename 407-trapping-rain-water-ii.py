import math
from typing import List
import heapq

class Solution:
    def trapRainWaterWrong(self, heightMap: List[List[int]]) -> int:
        m,n = len(heightMap), len(heightMap[0])

        min_vertical = [[math.inf for _ in range(n)] for _ in range(m)]
        for j in range(n):
            top_max = -math.inf
            for i in range(m):
                if heightMap[i][j] > top_max:
                    top_max = heightMap[i][j]
                    min_vertical[i][j] = top_max

        for j in range(n):
            bottom_max = -math.inf
            for i in reversed(range(m)):
                if heightMap[i][j] > bottom_max:
                    bottom_max = heightMap[i][j]
                min_vertical[i][j] = min(min_vertical[i][j], bottom_max)

        result = 0
        for i in range(m):
            left,right = 0, n-1
            left_max = heightMap[i][left]
            right_max = heightMap[i][right]
            while left < right:
                if heightMap[i][left] < heightMap[i][right]:
                    left_max = max(left_max, heightMap[i][left])
                    result += min(left_max, min_vertical[i][left]) - heightMap[i][left]
                    left += 1
                else:
                    right_max = max(right_max, heightMap[i][right])
                    result += min(right_max, min_vertical[i][right]) - heightMap[i][right]
                    right -= 1

        return result
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        heap = []
        m,n = len(heightMap), len(heightMap[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            heapq.heappush(heap, (heightMap[i][0], (i,0)))
            heapq.heappush(heap, (heightMap[i][n-1], (i,n-1)))
            visited[i][0] = True
            visited[i][n-1] = True
        for i in range(n):
            heapq.heappush(heap, (heightMap[0][i], (0,i)))
            heapq.heappush(heap, (heightMap[m-1][i], (m-1, i)))
            visited[0][i] = True
            visited[m-1][i] = True


        result = 0
        while heap:
            height, (x,y) = heapq.heappop(heap)
            for i,j in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                if i < 0 or i >= m or j < 0 or j >= n or visited[i][j]:
                    continue
                result += max(0, height - heightMap[i][j])
                visited[i][j] = True
                heapq.heappush(heap, (max(heightMap[i][j], height), (i,j)))

        return result
def main():
  sol = Solution()
  print(sol.trapRainWater(
                        [[1,4,3,1,3,2],
                        [3,2,1,3,2,4],
                        [2,3,3,2,3,1]]))

if __name__ == "__main__":
  main()

"""
    [1,4,3,1,3,2],
    [3,2,1,3,2,4],
    [2,3,3,2,3,1],

top_max
    [1,4,3,1,3,2]
    [3,4,3,3,3,4]
    [3,3,3,3,3,4]
bottom_max
    [3,4,3,3,3,4]
    [3,3,3,3,3,4]
    [2,3,3,2,3,1]
min_vertical
    [1,4,3,1,3,2]
    [3,3,3,3,3,4]
    [2,3,3,2,3,1]

result
    [0,0,0,0,0,0]
    [0,1,2,0,1,0]
    [0,0,0,0,0,0]
sum(result) = 7
"""
