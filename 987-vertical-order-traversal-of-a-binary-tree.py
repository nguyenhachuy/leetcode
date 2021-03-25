# Definition for a binary tree node.
from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        table = defaultdict(lambda: defaultdict(list))
        def rcs(root, row, col):
            if not root:
                return

            row_dict = table[col][row]
            row_dict.append(root.val)

            rcs(root.left, row+1, col-1)
            rcs(root.right, row+1, col+1)

        result = []
        rcs(root, 0, 0)
        for col in sorted(table.keys()):
            col_dict = table[col]
            temp = []
            for row in sorted(col_dict.keys()):
                temp.extend(sorted(col_dict[row]))
            if temp:
                result.append(temp)
        return result



"""
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

traverse tree and record by column, sort by row then by val

"""
