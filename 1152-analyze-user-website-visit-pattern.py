"""
We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i].

A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.  (The websites in a 3-sequence are not necessarily distinct.)

Find the 3-sequence visited by the largest number of users. If there is more than one solution, return the lexicographically smallest such 3-sequence.

Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"],
timestamp = [1,2,3,4,5,6,7,8,9,10],
website = ["home","about","career","home","cart","maps","home","home","about","career"]

Output: ["home","about","career"]
Explanation:
The tuples in this example are:
["joe", 1, "home"]
["joe", 2, "about"]
["joe", 3, "career"]
["james", 4, "home"]
["james", 5, "cart"]
["james", 6, "maps"]
["james", 7, "home"]
["mary", 8, "home"]
["mary", 9, "about"]
["mary", 10, "career"]
The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.

each user, sort, then find all possible paths

["h","eiy","cq","h","cq","txldsscx","cq","txldsscx","h","cq","cq"]
[527896567,334462937,517687281,134127993,859112386,159548699,51100299,444082139,926837079,317455832,411747930]
["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"]

"""
from typing import List
from collections import defaultdict

class Solution:
    def generate_pairs(self, visited, newest_website):
        result = []
        for visited_web in visited:
            result.append((visited_web, newest_website))

        return result

    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        request_infos = zip(username, timestamp, website)
        request_infos = sorted(request_infos, key=lambda x: (x[0],x[1],x[2]))

        three_sequences = defaultdict(set)
        visited = defaultdict(list)
        pairs = defaultdict(list)

        for request in request_infos:
            user, time, web = request
            for pair in pairs[user]:
                sequence = (pair[0], pair[1], web)
                # if sequence[0] == sequence[1] == sequence[2]:
                #     continue
                three_sequences[sequence].add(user)

            new_pairs = self.generate_pairs(visited[user], web)
            pairs[user].extend(new_pairs)
            visited[user].append(web)

        max_freq = 0
        result = ""
        for k,v in three_sequences.items():
            if len(v) > max_freq or (len(v) == max_freq and k < result):
                result = k
            max_freq = max(max_freq, len(v))

        return list(result)

def main():
    sol = Solution()
    # username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
    # timestamp = [1,2,3,4,5,6,7,8,9,10]
    # website = ["home","about","career","home","cart","maps","home","home","about","career"]

    # print(sol.mostVisitedPattern(username, timestamp, website))

    print(sol.mostVisitedPattern(
        ["h","eiy","cq","h","cq","txldsscx","cq","txldsscx","h","cq","cq"],
        [527896567,334462937,517687281,134127993,859112386,159548699,51100299,444082139,926837079,317455832,411747930],
        ["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"]
    ))

if __name__ == "__main__":
    main()
