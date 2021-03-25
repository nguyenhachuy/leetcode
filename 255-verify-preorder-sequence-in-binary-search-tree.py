"""
Given an array of unique integers preorder, return true if it is the correct preorder traversal sequence of a binary search tree.

when reconstruct the tree. left subtree < root < right subtree
preorder -> root left right
use a decreasing stack, because it's preorder, we must go all left and once we find a number > top of stack
that means we're going right
"""

import math
from collections import deque

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        lower_bound = -math.inf
        st = []

        for node in preorder:
            if node < lower_bound:
                return False
            while st and st[-1] < node:
                lower_bound = st.pop()

            st.push(node)

        return True
