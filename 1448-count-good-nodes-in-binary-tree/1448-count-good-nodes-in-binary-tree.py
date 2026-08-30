# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxi):
            if not node:
                return 0

            count = 0

            if node.val >= maxi:
                count = 1
                maxi = node.val

            left = dfs(node.left, maxi)
            right = dfs(node.right, maxi)

            count += left + right

            return count

        return dfs(root, root.val)
        