#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> list[int]:

        path = []

        def dfs(node: TreeNode) -> bool:
            if not node:
                return False
            path.append(node)
            if target == node:
                return True
            
            if not (dfs(node.left) or dfs(node.right)):
                path.pop()
                return False
            else:
                return True

        if not dfs(root):
            return []

        res = []
        def childrenK(node: TreeNode, K: int, exclude: TreeNode) -> None:
            if not node:
                return

            if K == 0:
                res.append(node.val)
            if node.left != exclude and K > 0:
                childrenK(node.left, K - 1, None)
            if node.right != exclude and K > 0:
                childrenK(node.right, K - 1, None)

        exclude = None
        while K >= 0 and path:
            node = path.pop()
            childrenK(node, K, exclude)
            K -= 1
            exclude = node

        return res

# @lc code=end

