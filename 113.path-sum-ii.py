#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from copy import copy


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def findPath(
            node: TreeNode, curSum: int,
            curPath: List[int], paths: List[List[int]]
        ) -> None:
            if node is None:
                return

            curPath.append(node.val)
            curSum += node.val

            if node.left is None and node.right is None and curSum == sum:
                paths.append(curPath)
            else:
                findPath(node.left, curSum, copy(curPath), paths)
                findPath(node.right, curSum, copy(curPath), paths)

        paths = []
        findPath(root, 0, [], paths)

        return paths

# @lc code=end
