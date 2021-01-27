"""
Given a string s and an integer k. You should construct k non-empty palindrome strings using all the characters in s.

Return True if you can use all the characters in s to construct k palindrome strings or False otherwise.

deconstruct string into char freq

to be palindrome, must have even number of chars + 1
can have 0...k odd freq but no more

Input: s = "annabelle", k = 2
a:2, n:2,b:1,e:2,l:2
Input: s = "leetcode", k = 3
l:1,e:3,t:1,c:1,o:1,d:1
Input: s = "cr", k = 7
not enough strings

odds <= k <= n
if more odds than k, we have too many strings
if k > n, we dont have enough characters to make

"""
from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        freq = Counter(s)
        if len(s) < k:
            return False
        odds = 0
        for _,v in freq.items():
            if v % 2 == 1:
                odds += 1
        return odds <= k
