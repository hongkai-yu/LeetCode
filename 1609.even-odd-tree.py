#
# @lc app=leetcode id=1609 lang=python3
#
# [1609] Even Odd Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from itertools import chain


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        def validateLevel(prevNodes: List[TreeNode], isEvenIndexed: bool) -> bool:
            
            nodesLevel = []
            for node in prevNodes:
                if node.left: nodesLevel.append(node.left)
                if node.right: nodesLevel.append(node.right)
            
            if not nodesLevel: return True

            if isEvenIndexed:
                if not all([node.val % 2 == 1 for node in nodesLevel]): return False
                if not all([nodesLevel[i].val < nodesLevel[i+1].val for i in range(len(nodesLevel) - 1)]): return False
            else:
                if not all([node.val % 2 == 0 for node in nodesLevel]): return False
                if not all([nodesLevel[i].val > nodesLevel[i+1].val for i in range(len(nodesLevel) - 1)]): return False
            
            return validateLevel(nodesLevel, not isEvenIndexed)
        return root.val % 2 == 1 and validateLevel([root], False)


        
# @lc code=end

