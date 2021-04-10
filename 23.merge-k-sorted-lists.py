#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            mid = len(lists) // 2
            return self.merge2Lists(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:]))
        
    def merge2Lists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1 or not list2:
            return list1 or list2
        
        if list1.val <= list2.val:
            list1.next = self.merge2Lists(list1.next, list2)
            return list1
        else:
            list2.next = self.merge2Lists(list2.next, list1)
            return list2




        # start = mergedCursor = ListNode()

        # candidates = [l.val if l else None for l in lists]
        # while any(l is not None for l in lists):

        #     minValue = min(value for value in candidates if value is not None)
        #     # assert minValue != None
        #     minIndex = candidates.index(minValue)

        #     mergedCursor.next = lists[minIndex]
        #     mergedCursor = mergedCursor.next

        #     lists[minIndex] = lists[minIndex].next
        #     candidates[minIndex] = lists[minIndex].val if lists[minIndex] else None

        # return start.next


# @lc code=end
