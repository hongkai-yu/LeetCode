#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            else:
                node = stack.pop()
                res.append(node.val)
                root = node.right
        return res
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     res = []
    #     self.bfs(root, res)
    #     return res

    # def bfs(self, node: 'TreeNode', res: List[int]) -> None:
    #     if not node:
    #         return
    #     self.bfs(node.left, res)
    #     res.append(node.val)
    #     self.bfs(node.right, res)


        
# @lc code=end

