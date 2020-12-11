class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # count X in start and end --> should be the same
        if start.count('X') != end.count('X'):
            return False

        n = len(start)
        i = j = 0 # Start at the beginning of both strings
        while (i < n and j < n):
            while i < n and start[i] == 'X': #Skip all X
                i += 1
            while j < n and end[j] == 'X': #Skip all X
                j += 1

            # i and j are the indices representing the next
            # occurrences of non-X characters
            if i == n or j == n:
                return i == n and j == n #If both reach the end we're good, if not it's not equal

            if start[i] != end[j]: #If we reach a string that's not equal, we cannot
                return False
            if start[i] == 'L' and i < j: # Both are L but the final L is to the RIGHT of the original L, L can only move left so this is impossible
                return False
            if start[i] == 'R' and i > j: # Both are R but the final R is to the LEFT of the original R, R can only move right so this is impossible
                return False

            i += 1
            j += 1

        return True
