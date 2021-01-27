from collections import defaultdict

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append((timestamp, value))

    def binary_search(self, values, target_timestamp):
        i,j = 0, len(values)-1
        result = ""
        while i <= j:
            mid = i + (j-i)//2
            if values[mid][0] <= target_timestamp:
                result = values[mid][1]
                i = mid + 1
            elif values[mid][0] > target_timestamp:
                j = mid - 1
        return result

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.table:
            return ""
        return self.binary_search(self.table[key], timestamp)


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


def main():
    kv = TimeMap()
    print(kv.set("foo", "bar", 1))
    print(kv.get("foo", 1))
    print(kv.get("foo", 3))
    print(kv.set("foo", "bar2", 4))
    print(kv.get("foo", 4))
    print(kv.get("foo", 5))
if __name__ == "__main__":
  main()
