#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        visited = set()

        def dfs(room: int) -> bool:
            if room in visited:
                return False
            visited.add(room)

            if len(visited) == N:
                return True

            return any(dfs(key) for key in rooms[room])

        return dfs(0)
        
# @lc code=end

