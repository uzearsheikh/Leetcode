from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        result = []
        queue = deque([])
        queue.append(root)

        while len(queue) > 0:
            e = []

            for i in range(len(queue)):
                node = queue.popleft()

                e.append(node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            result.append(e)

        return result