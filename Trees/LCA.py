class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node,res,resl):
            if not node:
                return
            if node.val==p.val:
                resl.append(res+[p.val])
            if node.val==q.val:
                resl.append(res+[q.val])
            dfs(node.left,res+[node.val],resl)
            dfs(node.right,res+[node.val],resl)
        resl=[]
        dfs(root,[],resl)
        i,j=0,0
        minu=min(len(resl[0]),len(resl[1]))
        while i < len(resl[0]) and j < len(resl[1]):
            if resl[0][i]!=resl[1][j]:
                return TreeNode(resl[0][i-1])
            i+=1
            j+=1
        return TreeNode(resl[0][minu-1])