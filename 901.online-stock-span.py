#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#

# @lc code=start
class StockSpanner:

    def __init__(self):
        self.priceStack = [] # from old to new, elements (price, span)
        

    def next(self, price: int) -> int:
        span = 1

        while self.priceStack:
            p, s = self.priceStack[-1]
            if price >= p:
                span += s
                self.priceStack.pop()
            else: break

        self.priceStack.append((price, span))

        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end

if __name__ == "__main__":
    s = StockSpanner()

    for i in range(10000):
        print(s.next(i // 100 + 1))
