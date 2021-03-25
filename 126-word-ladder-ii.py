"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"

sounds like a "find shortest path problem" where each node is a word
and there's an edge if the edit distance is 1

all words are same length. -> word count + word order
1 <= beginWord.length <= 10

1 is BFS, we can even do a 2 way BFS. Path is important so each traversal must retain path

regardless, we can precompute the edges. how to compute edges efficiently. hit -> *it, h*t, hi*

let's say we do BFS, ending condition is ending word, to keep path we keep a "node" with list of words so far

"""
from collections import defaultdict
from collections import deque
from typing import List

class Solution:
    # Solution from LC
    def findLadders(self,beginWord, endWord, wordList):
    tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
    if endWord not in wordList: return []
    found, bq, eq, nq, rev = False, {beginWord}, {endWord}, set(), False
    while bq and not found:
        words -= set(bq)
        for x in bq:
            for y in [x[:i]+c+x[i+1:] for i in range(n) for c in 'qwertyuiopasdfghjklzxcvbnm']:
                if y in words:
                    if y in eq:
                        found = True
                    else:
                        nq.add(y)
                    tree[y].add(x) if rev else tree[x].add(y)
        bq, nq = nq, set()
        if len(bq) > len(eq):
            bq, eq, rev = eq, bq, not rev

    # Concise backtracking function but we can use a regular backtrackign to traverse the "tree" and
    # output the paths

    def bt(x):
        return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]
    return bt(beginWord)
    def create_edges(self, wordList):
        table = defaultdict(list)
        for word_index, word in enumerate(wordList):
            for i in range(len(word)):
                pattern = f"{word[:i]}*{word[i+1:]}"
                table[pattern].append(word_index)

        return table

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        graph = self.create_edges(wordList)

        q = deque()
        q.append((beginWord, [beginWord]))
        result = []

        found_path = False

        while q:
            second_q = deque()

            current_word, path = q.popleft()

            if current_word == endWord:
                result.append(path)
                found_path = True
                continue

            if found_path:
                continue
            # print(f"current word {current_word}")
            patterns = [f"{current_word[:i]}*{current_word[i+1:]}" for i in range(len(current_word))]

            for pattern in patterns:
                for next_word_index in graph[pattern]:
                    next_word = wordList[next_word_index]
                    if next_word in path:
                        continue
                    second_q.append((next_word, path+[next_word]))
            q = second_q
            if len(result) > 0:
                break

        return result

import unittest

class Test(unittest.TestCase):

    def test_1(self):
        cases = [
            ["hit", "cog", ["hot","dot","dog","lot","log","cog"], [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]],
            ["hit", "cog", ["hot","dot","dog","lot","log"], []]
        ]
        sol = Solution()
        for beginWord, endWord, wordList, answer in cases:
            self.assertEqual(sol.findLadders(beginWord, endWord, wordList), answer)

if __name__ == '__main__':
    unittest.main()




