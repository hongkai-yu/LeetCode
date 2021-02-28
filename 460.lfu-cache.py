#
# @lc app=leetcode id=460 lang=python3
#
# [460] LFU Cache
#

# @lc code=start
import heapq
from queue import PriorityQueue


class LFUCache:

    class Node:
        def __init__(self, key: int, value: int, isRoot: bool = False):
            self.key = key
            self.value = value
            self.freq = 0 if isRoot else 1
            self.prev = None
            self.next = None

        def addFreq(self) -> None:
            self.freq += 1
            self._sink()

        def insert(self, node: "Node") -> None:
            self.next, self.next.prev, node.prev, node.next = node, node, self, self.next
            node._sink()

        def pop(self) -> "Node":
            nextNode = self.next

            assert nextNode

            self.next = nextNode.next
            if nextNode.next: nextNode.next.prev = self

            return nextNode

        def _sink(self) -> None:
            if not self.next: return 
            
            if self.freq >= self.next.freq:
                self._swapNext() 
                self._sink()

        def _swapNext(self) -> None:
            if not self.next: return

            nextNode = self.next
            self.prev.next = nextNode
            self.prev, self.next, nextNode.prev, nextNode.next = nextNode, nextNode.next, self.prev, self
            if self.next: self.next.prev = self

    def __init__(self, capacity: int):
        self.CAPACITY = capacity
        self.dictCache = {}
        self.root = self.Node(-1, -1, isRoot=True)

    def get(self, key: int) -> int:
        if key in self.dictCache:
            node = self.dictCache[key]
            node.addFreq()
            return node.value

        else: return -1

    def put(self, key: int, value: int) -> None:
        if self.CAPACITY == 0: return

        if key in self.dictCache:
            node = self.dictCache[key]
            node.value = value
            node.addFreq()
        else:
            if len(self.dictCache) == self.CAPACITY:
                del self.dictCache[self.root.pop().key]

            node = self.Node(key, value)
            self.dictCache[key] = node
            self.root.insert(node)

if __name__ == "__main__":
    cache = LFUCache(2)
    cache.put(2,1)
    cache.put(1,1)
    cache.put(2,3)
    cache.put(4,1)
    print(cache.get(1))
    print(cache.get(2))

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
