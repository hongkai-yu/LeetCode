#
# @lc app=leetcode id=993 lang=python3
#
# [993] Cousins in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import deque


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        parentLevel = []

        queue = deque([(root, None, 0)])

        while queue:

            node, parent, depth = queue.popleft()


            if parentLevel and parentLevel[1] != depth:
                return False

            if node.val in [x, y]:
                if parentLevel:
                    return parent != parentLevel[0] # and depth == parentLevel[1]
                else:
                    parentLevel = [parent, depth]
                    # no need to append
            else:
                if node.left:
                    queue.append((node.left, node, depth + 1))
                if node.right:
                    queue.append((node.right, node, depth + 1))

        return False

                
        
# @lc code=end

