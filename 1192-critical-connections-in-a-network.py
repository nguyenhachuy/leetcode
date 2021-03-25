"""
https://www.youtube.com/watch?v=RYaakWv5m6o
Key observation: maintaining a discovery and lowest mapping, we discover a cycle if we see a node with lower discovery.
The lowest/earliest node discoverable will propagate throughout the entire cycle
We can also do subtraction to find "gap"

discovery + lowest + graph -> O(V+E) space
each node is visited once, and each edge is visited once -> O(V+E)
"""
from collections import defaultdict

class Solutions:
  def __init__(self):
      self.counter = 0
  def DFS(self, discovery, lowest, node, graph, prev):
    lowest[node] = self.counter
    discovery[node] = self.counter
    self.counter += 1

    results = []
    for neighbor in graph[node]:
      if neighbor == prev:
          continue
      if neighbor not in discovery:
          results += self.DFS(discovery, lowest, neighbor, graph, node)
      lowest[node] = min(lowest[neighbor], lowest[node])

      if lowest[neighbor] > discovery[node]:
          results += [[neighbor, node]]

    return results

  def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
    if not connections:
      return connections

    discovery = {}
    lowest = {}
    graph = defaultdict(list)
    self.counter = 0
    for connection in connections:
      x,y = connection
      graph[x].append(y)
      graph[y].append(x)

    return self.DFS(discovery, lowest, 0, graph, -1)

class Solution:
  def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
      def dfs(rank, curr, prev):
          low[curr], result = rank, []
          for neighbor in edges[curr]:
              if neighbor == prev: continue
              if not low[neighbor]:
                  result += dfs(rank + 1, neighbor, curr)
              low[curr] = min(low[curr], low[neighbor])
              if low[neighbor] >= rank + 1:
                  result.append([curr, neighbor])
          return result

      low, edges = [0] * n, collections.defaultdict(list)
      for u, v in connections:
          edges[u].append(v)
          edges[v].append(u)

      return dfs(1, 0, -1)



"""
discovery {0:0, 1:1, 2:2, 3:3}
lowest {0:0, 1:0, 2:0, 3:0}
graph {0: [1,2], 1: [0,2,3], 2: [1,0], 3: [1]}
counter 0

0
result []

  1
  result []

    2
    result []

    3
    result []

"""
def main():
  sol = Solutions()
  print(sol.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))

if __name__ == "__main__":
  main()

