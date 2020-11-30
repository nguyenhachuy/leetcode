class Solution:
    def readValues(self, root, values):
        if not root:
            return
        values.add(root.val)
        self.readValues(root.left, values)
        self.readValues(root.right, values)
        
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        if not root1 or not root2:
            return False
        values1 = set()
        self.readValues(root1, values1)
        st = [root2]
        while st:
            node = st.pop()
            if (target - node.val) in values1:
                return True
            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)
        
        return False

