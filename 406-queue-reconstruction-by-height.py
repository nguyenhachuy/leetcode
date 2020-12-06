from typing import List
from operator import itemgetter
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sorted_people = sorted(people, key=lambda x: (x[0], -x[1]))

        result = []
        for i in reversed(range(len(sorted_people))):
            result.insert(sorted_people[i][1], sorted_people[i])
        return result

def main():
    sol = Solution()
    print(sol.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
if __name__ == "__main__":
  main()

"""
2:23, finish 3:04 with solution =.=
1 <= people.length <= 2000
0 <= hi <= 106
0 <= ki < people.length
It is guaranteed that the queue can be reconstructed.

Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]


"""
