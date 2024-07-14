class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p ==None or q == None:
             return p == q
        return p.val == q.val and self.isSameTree(p.left , q.left) and self.isSameTree(p.left , q.left)