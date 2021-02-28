#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        evenHead = head.next

        oddCursor = head
        evenCursor = head.next
        curOdd = False
        while(True):
            if curOdd:
                if not oddCursor.next: break
                evenCursor.next = oddCursor.next
                evenCursor = oddCursor.next
                curOdd = False
            else:
                if not evenCursor.next: break
                oddCursor.next = evenCursor.next
                oddCursor = evenCursor.next
                curOdd = True
        oddCursor.next = evenHead
        evenCursor.next = None
        return head

        
# @lc code=end

