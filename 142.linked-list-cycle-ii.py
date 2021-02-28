#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        visited = set()
        curNode = head
        
        while(curNode):
            if curNode in visited: return curNode
            else:
                visited.add(curNode)
                curNode = curNode.next

        return None
        
# @lc code=end

