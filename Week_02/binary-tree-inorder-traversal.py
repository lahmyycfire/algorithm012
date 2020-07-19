class Solution:
    # 迭代
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        cur = root
        res = []

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

        return res
        
    # 递归
    def inorder(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        return self.inorder(self.left) + [root.val] + self.inorder(self.right)