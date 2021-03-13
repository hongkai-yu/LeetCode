#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        start = ListNode()
        cursor = start
        carry = 0
        while (l1 or l2 or (carry != 0)):
            s = carry
            if l1: s += l1.val
            if l2: s += l2.val
            cursor.next = ListNode(s % 10)

            carry = s // 10
            cursor = cursor.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return start.next


        
# @lc code=end

