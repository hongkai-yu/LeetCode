#
# @lc app=leetcode id=382 lang=python3
#
# [382] Linked List Random Node
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from random import randrange

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        
        # node = head
        # size = 0
        # while node:
        #     size += 1
        #     node = node.next
        # self.size = size

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        # n = randrange(self.size)

        # node = self.head
        # for i in range(n):
        #     node = node.next
        # return node.val

        reservoir = self.head
        node = self.head.next
        idx = 1
        while node:
            idx += 1 
            rdm = randrange(idx)
            if rdm == 0:
                reservoir = node
            node = node.next
        return reservoir.val
            

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end

