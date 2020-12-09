class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for num in asteroids:
            while result and result[-1] > 0 and num < 0 and abs(result[-1]) < abs(num):
                result.pop()
            if result and result[-1] > 0 and num < 0:
                if (abs(result[-1]) == abs(num)):
                    result.pop()
            else:
                result.append(num)
        return result

