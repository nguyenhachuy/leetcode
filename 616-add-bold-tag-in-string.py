from collections import defaultdict

class TrieNode:
    def __init__(self, char, is_word):
        self.is_word = is_word
        self.char = char
        self.neighbors = {}

class Trie:
    def __init__(self):
        self.head = TrieNode("", False)
    def add_word(self, word):
        temp = self.head

        for c in word:
            if c not in temp.neighbors:
                temp.neighbors[c] = TrieNode(c, False)
            temp = temp.neighbors[c]
        temp.is_word = True

    def match_word(self, word):
        temp = self.head
        length = 0
        for i,c in enumerate(word):
            if c in temp.neighbors:
                temp = temp.neighbors[c]
                if temp.is_word == True:
                    length = i+1
            else:
                return length
        return length

class Solution:
    def addBoldTag(self, s: str, dict: list[str]) -> str:
        if not dict:
            return s
        trie = Trie()
        for w in dict:
            trie.add_word(w)

        intervals = []
        for i,v in enumerate(s):
            max_interval_from_here = trie.match_word(s[i:])
            if max_interval_from_here > 0:
                if intervals and intervals[-1][1] >= i:
                    intervals[-1][1] = max(intervals[-1][1], i+max_interval_from_here)
                else:
                    intervals.append([i, i+max_interval_from_here])

        if not intervals:
            return s
        result = []

        if intervals[0][0] > 0:
            result.append(s[:intervals[0][0]])
        for i in range(len(intervals)):
            result.append(s[intervals[i-1][1]:intervals[i][0]])
            result.append("<b>")
            result.append(s[intervals[i][0]:intervals[i][1]])
            result.append("</b>")

        if intervals and intervals[-1][1] < len(s):
            result.append(s[intervals[-1][1]:])

        return "".join(result)

def main():
    sol = Solution()
    cases = [
        ["abcxyz123", ["abc","123"]],
        ["aaabbcc", ["aaa","aab","bc"]],
        ["aaabbcc", ["aaa","aab","bc","aaabbcc"]]
    ]
    for s,d in cases:
        print(sol.addBoldTag(s,d))

if __name__ == "__main__":
    main()

"""
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b>
to wrap the substrings in s that exist in dict. If two such substrings overlap,
you need to wrap them together by only one pair of closed bold tag.
Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.

generate intervals, then merge the intervals if they overlap
then form string based on disjoint intervals
"""
