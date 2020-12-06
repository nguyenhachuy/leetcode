from typing import List
class Solution:
    def bfs(self, grid, q):
        visited = set(q)
        distance = 0
        m,n = len(grid), len(grid[0])
        while q:
            second_q = []
            while q:
                a,b = q.pop()
                grid[a][b] = min(grid[a][b], distance)
                for c,d in ((a+1,b),(a-1,b),(a,b+1),(a,b-1)):
                    if c >= 0 and c < m and d >= 0 and d < n and grid[c][d] > 0 and (c,d) not in visited:
                        visited.add((c,d))
                        second_q.append((c,d))
            distance += 1
            q = second_q


    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        m,n = len(rooms), len(rooms[0])
        q = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i,j))

        self.bfs(rooms, q)

def main():
    sol = Solution()
    matrix = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    sol.wallsAndGates(matrix)
    print(matrix)
if __name__ == "__main__":
  main()
