from typing import List
class Solution:
    def check_lt(self, word1, word2, order):
        i = 0
        for i in range(min(len(word1), len(word2))):
            o1 = order[word1[i]]
            o2 = order[word2[i]]
            if o2 < o1:
                return False
            elif o1 < o2:
                return True

            i += 1
        return len(word1) <= len(word2)

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {}
        for i,v in enumerate(order):
            order_dict[v] = i
        for i in range(1, len(words)):
            if not self.check_lt(words[i-1], words[i], order_dict):
                return False

        return True

def main():
    sol = Solution()
    print(sol.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
    print(sol.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))
if __name__ == "__main__":
    main()



"""
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
"""
