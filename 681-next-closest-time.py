import bisect

class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = []
        for c in time:
            if c.isdigit():
                digits.append(c)

        le_6 = [x for x in digits if x < 6]
        le_2 = [x for x in digits if x <= 2]

        hour, minutes = time.split(":")
        next_closest_single_minute = bisect.bisect_left(digits, minutes[-1] + 1)
        if next_closest_single_minute < len(digits):
            return time[:-1] + digits[next_closest_single_minute]

        next_closest_double_minute = len(le_2)
        if len(minutes) == 2:
            next_closest_double_minute = bisect.bisect_left(le_2, minutes[-2] + 1)
            if next_closest_double_minute < len(le_2) and next_closest_single_minute < len(digits):
                return hour + ":" + le_2[next_closest_double_minute] + digits[next_closest_single_minute]

        next_closest_single_hour = bisect.bisect_left(digits, hour[-1] + 1)
        if next_closest_single_hour < len(digits):
            
def main():
  sol = Solutions()
  print(sol.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))

if __name__ == "__main__":
  main()


"""
hour = 0,1,2
hour2 = 
"""