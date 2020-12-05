import collections

class Solution:
    def pacificAtlantic(self, matrix: list[list[int]]) -> list[list[int]]:
        pacific = [[False] * len(matrix[0]) for _ in range(len(matrix))]      
        atlantic = [[False] * len(matrix[0]) for _ in range(len(matrix))]

        pacific_q = [(0, x) for x in range(len(matrix[0]))]
        atlantic_q = [(len(matrix)-1, x) for x in range(len(matrix[0]))]
        pacific[0] = [True] * len(matrix[0])
        atlantic[-1] = [True] * len(matrix[0])
        for i in range(1, len(matrix)):
            pacific_q.append((i, 0))
            pacific[i][0] = True
        for i in range(len(matrix)-1):
            atlantic_q.append((i, len(matrix[0])-1))
            atlantic[i][len(matrix[0])-1] = True
        def bfs(matrix, visited, q):
            while q:
                x,y = q.pop()
                for next_x, next_y in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                    if next_x >= 0 and next_x < len(matrix) and next_y >= 0 and next_y < len(matrix[0]) and not visited[next_x][next_y] and matrix[next_x][next_y] > matrix[x][y]:
                        visited[next_x][next_y] = True
                        q.appendleft((next_x, next_y))
        bfs(matrix, pacific, collections.deque(pacific_q))
        bfs(matrix, atlantic, collections.deque(atlantic_q))

        result = []
        print(pacific)
        print(atlantic)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i,j])

        return result


def main():
    sol = Solution()
    print(sol.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
if __name__ == "__main__":
    main()




