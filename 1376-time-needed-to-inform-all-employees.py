class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        neighbors = defaultdict(list)
        for i,v in enumerate(manager):
            neighbors[v].append(i)
        minute = 0
        q = [(headID, 0)]
        while q:
            second_q = []
            while q:
                node, time = q.pop()
                minute = max(minute, time)
                for neighbor in neighbors[node]:
                    second_q.append((neighbor, time+informTime[node]))
            q = second_q

        return minute

"""
layer by layer, and keep track of time from behind.
"""
