from typing import List
from collections import defaultdict

class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)

        for X,Y in relations:
            graph[Y].append(X)

        visiting = [False] * (N+1)
        visited = [False] * (N+1)
        rank = [1] * (N+1)
        def DFS(node):
            if visited[node]:
                return True
            if visiting[node]:
                return False

            visiting[node] = True

            for neighbor in graph[node]:
                cycle = DFS(neighbor)
                if not cycle:
                    return cycle
                rank[node] = max(rank[node], rank[neighbor] + 1)


            visited[node] = True
            visiting[node] = False

            return True

        for i in range(1,N+1):
            cycle = DFS(i)
            if not cycle:
                return -1

        return max(rank)

def main():
    sol = Solution()
    relations = [
        [[1,3],[2,3]],
        [[1,2],[2,3],[3,1]],
        [[1,2],[2,3]]
    ]
    for x in relations:
        print(sol.minimumSemesters(3, x))
if __name__ == "__main__":
    main()
