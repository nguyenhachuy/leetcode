"""
Given a set of words (without duplicates), find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y


Input:
["area","lead","wall","lady","ball"]

Output:
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

length of word determines the number of words in the group.
words must be same length, all words are guaranteed same length
order of words matter because we need to check for forms

use 1 word as anchor, then find the next word that match the prefix
when prefix is the entire word and we can find such word, we found a word square

"b all" requires "a", 1 word stat with a which is area"
"ba ll" requires "l", 1 word start with le which is lead or lady
"bal l" requires "l", 1 word start with lad which is ....

we need to check prefix a lot, we can use trie to match the word
backtracking to match the words, add to result when we find one

"""
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.neighbors = {}
        self.words = []

class Trie:
    def __init__(self, words):
        self.head = TrieNode("")
        self.words = words
        for index, word in enumerate(words):
            self.add_word(word, index)

    def add_word(self, word, index):
        temp = self.head
        for c in word:
            if c not in temp.neighbors:
                temp.neighbors[c] = TrieNode(c)
            temp = temp.neighbors[c]
            temp.words.append(index)

    def find_node(self, word):
        temp = self.head

        for c in word:
            if c not in temp.neighbors:
                return None

            temp = temp.neighbors[c]

        return temp

    def all_words_from_node(self, node):
        if not node:
            return []

        return [self.words[i] for i in node.words]
class Solution:
    def wordSquares(self, words: list[str]) -> list[list[str]]:
        trie = Trie(words)
        result = []


        def backtracking(sequence):
            if sequence and len(sequence) == len(sequence[-1]):
                result.append(sequence[:])
                return

            prefix = "".join((x[len(sequence)] for x in sequence))

            top_node = trie.find_node(prefix)
            if not top_node:
                return

            for next_word in trie.all_words_from_node(top_node):
                sequence.append(next_word)
                backtracking(sequence)
                sequence.pop()


        # import pudb; pu.db # Debug
        for i,w in enumerate(words):
            backtracking([w])

        return result

import unittest

class Test(unittest.TestCase):

    def test_1(self):
        cases = [
            [["ball","area","lead","lady"],
            [
              [ "ball",
                "area",
                "lead",
                "lady"
              ]
            ]],
            [["area","lead","wall","lady","ball"],
            [
              [ "wall",
                "area",
                "lead",
                "lady"
              ],
              [ "ball",
                "area",
                "lead",
                "lady"
              ]
            ]],
            [["abat","baba","atan","atal"],
            [
              [ "baba",
                "abat",
                "baba",
                "atan"
              ],
              [ "baba",
                "abat",
                "baba",
                "atal"
              ]
            ]],
            [["a"], [["a"]]],
            [["aa", "bb"], [['aa', 'aa'], ['bb', 'bb']]],
        ]
        sol = Solution()
        for words, answer in cases:
            self.assertEqual(sol.wordSquares(words), answer)

if __name__ == '__main__':
    unittest.main()

