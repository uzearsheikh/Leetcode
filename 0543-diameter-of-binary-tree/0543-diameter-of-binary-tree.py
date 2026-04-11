# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def depth(node):
            if node is None:
                return 0   # empty node ki height
            
            left = depth(node.left)
            right = depth(node.right)
            
            # update diameter (longest path through this node)
            self.diameter = max(self.diameter, left + right)
            
            # return height
            return max(left, right) + 1
        
        depth(root)
        return self.diameter
