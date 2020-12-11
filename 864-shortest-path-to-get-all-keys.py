class Solution:

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m,n = len(grid), len(grid[0])
        def BFS(start_x, start_y, key_map):
            visited = set([(start_x, start_y,0)])
            q = [(start_x, start_y, 0)]
            distance = 0
            while q:
                second_q = []
                while q:
                    i,j,state = q.pop()
                    if state == (2**len(key_map) - 1):
                        return distance
                    for a,b in ((i-1,j), (i+1,j),(i,j-1),(i,j+1)):
                        if a < 0 or a >= m or b < 0 or b >= n or grid[a][b] == "#":
                            continue
                        if (grid[a][b].isupper() and not bool(key_map[grid[a][b].lower()] & state)):
                            continue
                        next_state = state | key_map[grid[a][b]] if grid[a][b].islower() else state
                        if (a,b,next_state) in visited:
                            continue
                        second_q.append((a,b,next_state))
                        visited.add((a,b,next_state))
                distance += 1
                q = second_q
            return -1

        key_map = {}
        factor = 1
        start_x, start_y = 0,0
        for i in range(m):
            for j in range(n):
                if grid[i][j].islower():
                    key_map[grid[i][j]] = factor
                    factor = factor << 1
                elif grid[i][j] == "@":
                    start_x, start_y = i, j

        return BFS(start_x, start_y, key_map)
