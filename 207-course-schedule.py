from collections import defaultdict
from typing import List

class Solution:
    def DFS(self, course, graph, visited, st_set):
        visited.add(course)
        st_set.add(course)

        for n in graph[course]:
            if n in st_set or n == course:
                return True
            if n not in visited and self.DFS(n, graph, visited, st_set):
                return True


        st_set.remove(course)
        return False



    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for p in prerequisites:
            x,y = p
            graph[y].append(x)
        visited = set()
        for c in range(numCourses):
            if self.DFS(c, graph, visited, set()):
                return False

        return True

def main():
    sol = Solution()
    pairs = [
        [[[1,0]], 2],
        [[[1,0],[0,1]], 2]
    ]
    for s in pairs:
        print(sol.canFinish(s[1], s[0]))
if __name__ == "__main__":
  main()




