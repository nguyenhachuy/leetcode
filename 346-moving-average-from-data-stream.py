class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        self.avg = 0
        self.size = size

    def next(self, val: int) -> float:
        self.q.append(val)
        self.avg += val
        if len(self.q) > self.size:
            prev = self.q.popleft()
            self.avg -= prev
        return self.avg / len(self.q)
