import bisect
class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = [x for x in time if x != ":"]
        combinations = [x+y for x in digits for y in digits]

        hour, minutes = time.split(":")
        time_to_minutes = int(hour)*60 + int(minutes)
        min_diff = math.inf
        result = ""
        min_time = ""
        min_possible_time = math.inf
        for combination_a in combinations:
            for combination_b in combinations:
                if int(combination_a) < 24 and int(combination_b) < 60:
                    new_time_minutes = int(combination_a)*60 + int(combination_b)
                    if new_time_minutes < min_possible_time:
                        min_possible_time = new_time_minutes
                        min_time = combination_a + ":" + combination_b
                    if new_time_minutes > time_to_minutes and new_time_minutes - time_to_minutes < min_diff:
                        min_diff = abs(new_time_minutes - time_to_minutes)
                        result = combination_a + ":" + combination_b

        if not result:
            return min_time
        return result

"""
hour = 0,1,2
hour2 =
"""
