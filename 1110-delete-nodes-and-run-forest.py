# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        result = []
        def rcs(root):
            if not root:
                return
            root.left = rcs(root.left)
            root.right = rcs(root.right)

            if root.val in to_delete_set:
                if root.left:
                    result.append(root.left)
                if root.right:
                    result.append(root.right)
                return None
            return root

        base_case = rcs(root)
        if base_case:
            result.append(base_case)
        return result
