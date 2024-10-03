class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,target):
            if not node:
                return
            if not node.left and not node.right:
                if target-node.val==0:
                    return True
            return dfs(node.right,target-node.val) or dfs(node.left,target-node.val)
        return dfs(root,targetSum)