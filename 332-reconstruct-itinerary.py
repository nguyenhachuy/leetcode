from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for (a,b) in tickets:
            graph[a].append(b)
        for airport in graph:
            graph[airport].sort()

        path = ["JFK"]
        def backtracking(a, distance):
            if distance == len(tickets):
                return True
            if a not in graph:
                return False

            for i,b in enumerate(graph[a]):
                if not b:
                    continue
                graph[a][i] = ""
                path.append(b)
                result = backtracking(b, distance+1)
                if result:
                    return result
                path.pop()
                graph[a][i] = b
            return False

        backtracking("JFK", 0)
        return path

def main():
    sol = Solution()
    strings = [
        [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
        [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]],
    ]
    for s in strings:
        print(sol.findItinerary(s))
if __name__ == "__main__":
  main()





"""
construct graph of from/to tickets
sort list to keep shortest lexi order
at least 1 valid path, but can be invalid paths
must use all tickets
return path

we can do backtracking
when we visit all edges, that means we're done
can visit same airport multiple times


"""
