# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathDown(self,node,maxi):
        if not node:
            return 0
        left = max(0,self.maxPathDown(node.left,maxi))
        right = max(0,self.maxPathDown(node.right,maxi))
        maxi[0] = max(maxi[0],left+right+node.val)
        
        return max(left,right)+node.val


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        Maxi = [float('-inf')]
        self.maxPathDown(root,Maxi)
        return Maxi[0]