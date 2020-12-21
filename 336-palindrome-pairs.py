from typing import List

"""
trie node requirements:
lower case letters -> 26
at each node, track the ending suffix that are palindromes
track ending character that is a word
track index of that word if it is a word
search for a word
search for ending suffixes
search for postfix palindrome
"""
class TrieNode:
    def __init__(self, letter, word=False, index=None):
        self.letter = letter
        self.neighbors = [None] * 26
        self.suffix_palindomes = []
        self.word = word
        self.index = index
class Solution:
    def order(self, c):
        return ord(c) - ord('a')
    def is_palindrome(self, word, i, j):
        print("checking palindrome: ", word,i,j)
        if i > j or i >= len(word):
            return False
        while i <= j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True
    def find_word(self, word, root):
        temp = root
        for i in range(len(word)):
            c = word[i]
            order_c = self.order(c)
            if not temp.neighbors[order_c]:
                return None
            temp = temp.neighbors[order_c]
        return temp
    # Also track remaining suffixes
    def insert_word(self, word, root, index):
        temp = root
        for i in reversed(range(len(word))):
            c = word[i]
            order_c = self.order(c)
            if not temp.neighbors[order_c]:
                temp.neighbors[order_c] = TrieNode(c)
            if self.is_palindrome(word, 0, i-1):
                temp.neighbors[order_c].suffix_palindomes.append(index)
            temp = temp.neighbors[order_c]
        temp.word = True
        temp.index = index
    def find_valid_prefix(self, word, root):
        print("valid_prefix", word)
        temp = root
        result = []
        for i in reversed(range(len(word))):
            c = word[i]
            order_c = self.order(c)
            if not temp.neighbors[order_c]:
                return result
            temp = temp.neighbors[order_c]
            if temp.word and self.is_palindrome(word, i+1, len(word)-1):
                result.append(temp.index)
        print(result)
        print("end_valid_prefix")
        return result


    # def all_valid_suffixes(self, word):
    #     prefixes = []
    #     suffixes = []
    #     for i in range(len(word)-1):
    #         if self.is_palindrome(word, 0, i) and (i+1) < len(word):
    #             suffixes.append(i+1)
    #         if self.is_palindrome(word, 1+i, len(word)-1) and i-1 >= 0:
    #             prefixes.append(i-1)
    #     return [prefixes, suffixes]
    # def palindromePairs(self, words: List[str]) -> List[List[int]]:
    #     result = []
    #     lookup = {v:i for i,v in enumerate(words)}
    #     palindromes = {v:i for i,v in lookup.items() if self.is_palindrome(i, 0, len(i)-1)}
    #     for i, v in enumerate(words):
    #         if v == "":
    #             for palindrome_index in palindromes:
    #                 result.append([i, palindrome_index])
    #                 result.append([palindrome_index, i])
    #         revese_word = v[::-1]

    #         if revese_word in lookup and lookup[revese_word] != i:
    #             result.append([i, lookup[revese_word]])

    #         prefixes, suffixes = self.all_valid_suffixes(v)
    #         for prefix in prefixes:
    #             prefix_remainder = v[:prefix+1][::-1]
    #             if prefix_remainder in lookup:
    #                 result.append([lookup[prefix_remainer], i])
    #         for suffix in suffixes:
    #             suffix_remainder = v[suffix:][::-1]
    #             if suffix_remainder in lookup:
    #                 result.append([lookup[suffix_remainder], i])

    #     return result

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        root = TrieNode(None)
        result = []
        for i,w in enumerate(words):
            self.insert_word(w, root, i)

        for i,w in enumerate(words):
            print("i,w", i, w)
            node = self.find_word(w, root)
            # if not node:
            #     continue
            if node and node == root and node.word:
                for j in range(len(words)):
                    if j == i or not self.is_palindrome(words[j], 0, len(words[j])-1):
                        continue
                    result.extend([[i,j], [j,i]])
            if node and node.word and node.index != i:
                result.append([i, node.index])
            print("reverse ", result)
            if node:
                result.extend([[i,x] for x in node.suffix_palindomes])
            print("suffix ", result)
            result.extend([[i,x] for x in self.find_valid_prefix(w, root)])
            print("prefix ", result)
        return result
def main():
    sol = Solution()
    cases = [
    # ["abcd","dcba","lls","s","sssll"],
    # ["bat","tab","cat"],
    # ["a",""],
    # ["a","abc","aba",""],
    ["a","b","c","ab","ac","aa"]
    ]
    for c in cases:
        print(c, ": ", sol.palindromePairs(c))

if __name__ == "__main__":
    main()




"""
empty string, auto pair with anything
BF, O(n^2*W) go through each pair, combine, and check palindrome
abba
for single character, find ones that start with a or end if a
abbb -> needs a because removing a make this a palindrome
sssll -> needs l because
abcba
for each word, check if it is 1 character away from palindrome by running
palindrome(i+1,j) and palindrome(i, j-1)
then, store in a hash map the needed character, and from what end
if palindrome(i+1,j) is true, we need character at i and at the end
if palindrome(i,j-1) is true, we need character at j and at the beginning

for any word larger than 1, we need its reverse to make it
lls
sllls
sssll
llsssll
if pattern is monotone at one end, we just need the prefix of that monotone pattern,
and 0->many of the pattern as prefix for the other string
lsasl
"""
