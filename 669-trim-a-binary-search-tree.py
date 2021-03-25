class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None

        left = self.trimBST(root.left, low, high) if root.left else None
        right = self.trimBST(root.right, low, high) if root.right else None
        root.left = left
        root.right = right

        if not (low <= root.val <= high):
            return left or right

        return root

"""
Intuition

Let trim(node) be the desired answer for the subtree at that node. We can construct the answer recursively.

Algorithm

When
node.val > high
node.val > high, we know that the trimmed binary tree must occur to the left of the node. Similarly, when
node.val < low
node.val < low, the trimmed binary tree occurs to the right of the node. Otherwise, we will trim both sides of the tree.

"""
