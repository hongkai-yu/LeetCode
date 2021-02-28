#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from operator import attrgetter


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        nodeList = [head]
        
        node = head
        while (node.next):
            nodeList.append(node.next)
            node = node.next

        nodeList.sort(key=attrgetter('val'))
        for i in range(len(nodeList)):
            nodeList[i].next = nodeList[i+1] if i+1 < len(nodeList) else None

        return nodeList[0]

        
# @lc code=end

