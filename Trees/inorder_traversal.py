class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def helper(node):
            if not node:
                return
            helper(node.left)
            res.append(node.val)
            helper(node.right)
        res=[]
        helper(root)
        return res