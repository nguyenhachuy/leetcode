class Solution:
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

