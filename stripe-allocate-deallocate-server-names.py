"""
You're running a pool of servers where the servers are
numbered sequentially starting from 1. Over time, any
given server might explode, in which case its server
number is made available for reuse. When a new
server is launched, it should be given the lowest available number.

Write a function which, given the list of currently
allocated server numbers, returns the number of the next server to allocate.

For example, your function should behave something like the following:

>> next_server_number([5, 3, 1])
2
>> next_server_number([5, 4, 1, 2])
3
>> next_server_number([3, 2, 1])
4
>> next_server_number([2, 3])
1
>> next_server_number([])
1

Server names consist of an alphabetic host type (e.g. "apibox") concatenated with the server number,
with server numbers allocated as before (so "apibox1",
"apibox2", etc. are valid hostnames).

Write a name tracking class with two operations,
allocate(host_type) and deallocate(hostname).
The former should reserve and return the next
available hostname, while the latter should release
that hostname back into the pool.

# For example:
#
# >> tracker = Tracker.new()
# >> tracker.allocate("apibox")
# "apibox1"
# >> tracker.allocate("apibox")
# "apibox2"
# >> tracker.deallocate("apibox1")
# nil
# >> tracker.allocate("apibox")
# "apibox1"
# >> tracker.allocate("sitebox")
# "sitebox1"
"""
"""
first problem is minimum missing number. sort, then find gap?
[1,2,4] -> 1,2 in correct position. 4 is 1 smaller => first missing is 4-1 = 3
[1,2,4,5] -> if find a number in correct position, any number less than that is also in correct position. so go right
[4,5] -> 4 is off, record value and go left
[2,3,5] -> 3 is off, record

second problem is build up from first problem. we get the map k: host name, v: list of hosts
since we will refer to host value by key, makes sense to use a set

allocate: find first missing number, add to set, and return
deallocate: remove that number from set

-> allocate will be O(n), deallocate O(1)
"""
from typing import List
from collections import defaultdict

class Solution:
    def __init__(self):
        self.hosts = defaultdict(set)
    def firstMissingPositive(self, arr: List[int]) -> int:
        if not arr or 1 not in arr:
            return 1
        n = len(arr)
        if n == 1:
            return 2

        for i in range(len(arr)):
            if arr[i] <= 0 or arr[i] > n:
                arr[i] = 1

        for i in range(len(arr)):
            val = abs(arr[i])
            if val < n and arr[val] > 0:
                arr[val] *= -1
            elif val == n and arr[0] > 0:
                arr[0] *= -1

        for i in range(1, n):
            if arr[i] > 0:
                return i

        if arr[0] > 0:
            return n
        return n+1
    def allocate(self, server):
        next_host = self.firstMissingPositive(list(self.hosts[server]))
        self.hosts[server].add(next_host)

        return f'{server}{next_host}'
    def deallocate(self, server):
        host_number = int(server[-1])
        self.hosts[server[:-1]].remove(host_number)

def main():
    sol = Solution()
    arrays = [
        [5, 3, 1],
        [5, 4, 1, 2],
        [3, 2, 1],
        [2, 3],
        [],
    ]
    for arr in arrays:
        print(arr, sol.firstMissingPositive(arr))

    tracker = Solution()
    print(tracker.allocate("apibox"), "apibox1")
    print(tracker.allocate("apibox"), "apibox2")
    print(tracker.deallocate("apibox1"), "nil")
    print(tracker.allocate("apibox"), "apibox1")
    print(tracker.allocate("sitebox"), "sitebox1")

if __name__ == "__main__":
  main()
