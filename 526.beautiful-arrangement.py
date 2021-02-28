#
# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#

# @lc code=start
class Solution:
    def countArrangement(self, N: int) -> int:
        candidatesPosition = [{n for n in range(1, N + 1)
                                 if n % position == 0 or position % n == 0}
                               for position in range(1, N + 1)]
        
        arr = [0]
        def search(candidatesPosition: list[set], used: set, arr: list[int]) -> None:
            usedNumber = len(used)
            if usedNumber == N:
                arr[0] += 1
                return

            candidates = candidatesPosition[usedNumber] - used

            if not candidates: return
            else:
                for c in candidates:
                    used.add(c)
                    search(candidatesPosition, used, arr)
                    used.remove(c)
        search(candidatesPosition, set(), arr)
        return arr[0]
                    
            
# @lc code=end

if __name__ == "__main__":
    print(Solution().countArrangement(2))