# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self,node,diameter):
        if not node:
            return 0
        lh = self.helper(node.left,diameter)
        rh = self.helper(node.right,diameter)
        diameter[0] = max(diameter[0],lh+rh)
        return max(lh,rh)+1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        self.helper(root,diameter)
        return diameter[0]        